#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import distutils.spawn
import itertools
import imp
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib2

common_mark_dir = os.path.join(os.path.dirname(__file__), 'CommonMark')
spec_path = os.path.join(common_mark_dir, 'spec.txt')
sys.path.append(os.path.join(common_mark_dir, 'test'))
import spec_tests
import normalize

# Default config values here.
config_file_noext = 'config_local'
config_file = config_file_noext + '.py'
config = dict(
    gfm_oauth_token = '',
    # GFM off by default because it is too slow.
    run_all_disable = ['gfm'],
    timeout = 5
)
try:
    config_custom = imp.load_source(config_file_noext, config_file).config
    config.update(config_custom)
except IOError:
    # Config file not present.
    pass

def order(n):
    """Number of digits of decimal represntation of integer > 0"""
    return int(math.log10(n)) + 1

def stdin_stdout_to_html(command, stdin):
    """
    Convenience method for compilers that take input on stdin and output to stdout.

    If the command fails, or returns non 0, raises an exception.
    """
    process = subprocess.Popen(
        command,
        shell = False,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True
    )
    stdout, stderr = process.communicate(stdin)
    return stdout

class Compiler(object):
    @classmethod
    def available(cls):
        try:
            stdin_stdout_to_html(cls.command, '')
        except:
            return False
        else:
            return True

class Compilers(object):
    """
    All nested classes of this class represent markdown compilers and implement the static methods:

    - available
    - to_html
    """

    # List of all the compiler classes.
    # TODO DRY this up and look them up with instrospection.
    compiler_ids = [
        'blackfriday',
        'cmark',
        'commonmarkjs',
        'gfm',
        'hoedown',
        'kramdown',
        'lunamark',
        'markdown2',
        'markdown_pl',
        'markdownjs',
        'marked',
        'maruku',
        'multimarkdown',
        'pandoc',
        'peg_markdown',
        'rdiscount',
        'redcarpet',
        'showdown',
    ]

    class gfm(Compiler):
        """
        You **must** be authenticated to use this because this test suite has more than 50 tests.
        <ettp://developer.github.com/v3/#rate-limiting>
        - authenticated: 60 requests per hour
        - unauthenticated requests: 5000 requests per hour
        """
        url = 'https://api.github.com/markdown?access_token=' + config['gfm_oauth_token']
        @classmethod
        def to_html(cls, input):
            data = '{{"text":{},"mode":"gfm","context":"github/gollum"}}'.format(json.dumps(input))
            req = urllib2.Request(cls.url, data)
            try:
                response = urllib2.urlopen(req, timeout = config['timeout'])
            except urllib2.URLError, e:
                return 'CONNEXION ERROR: ' + str(e)
            return response.read()

        @classmethod
        def name(cls):
            return cls.__name__

    class CommandCompiler(Compiler):
        """
        Base class for compilers which use a command in PATH.
        """
        @classmethod
        def to_html(cls, input):
            return stdin_stdout_to_html(cls.command, input)

        @classmethod
        def name(cls):
            return cls.command

    class blackfriday(CommandCompiler): command = ['blackfriday-tool']
    class cmark(CommandCompiler): command = ['cmark']
    class hoedown(CommandCompiler): command = ['hoedown']
    class commonmarkjs(CommandCompiler): command = ['commonmark']
    class kramdown(CommandCompiler): command = ['kramdown']
    class lunamark(CommandCompiler): command = ['lunamark']
    class markdown2(CommandCompiler): command = ['markdown2']
    class markdown_pl(CommandCompiler): command = ['Markdown.pl']
    class markdownjs(CommandCompiler): command = ['md2html']
    class marked(CommandCompiler): command = ['marked']
    class maruku(CommandCompiler): command = ['maruku']
    class multimarkdown(CommandCompiler): command = ['multimarkdown']
    class pandoc(CommandCompiler): command = ['pandoc']
    class peg_markdown(CommandCompiler): command = ['peg-markdown']
    class rdiscount(CommandCompiler): command = ['rdiscount']
    class redcarpet(CommandCompiler): command = ['redcarpet']
    class showdown(CommandCompiler): command = ['node', 'showdown-wrapper.js']

def stdout_flush(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def run_tests(tests, compilers, args):
    total_tests = 0
    total_compilers = len(compilers)
    errors = [0] * total_compilers
    times = [0.0] * total_compilers
    tests = itertools.ifilter(lambda test: re.match(args.filter,
                              test['section']), tests)
    for test in tests:
        total_tests += 1
        single_test_errors = 0
        for i, compiler in enumerate(compilers):
            start_time = time.time()
            if i != 0 and i % 5 == 0:
                stdout_flush('  ')
            if not args.number or total == args.number:
                fail = False
                try:
                    if (normalize.normalize_html(compiler.to_html(test['markdown'])) !=
                        normalize.normalize_html(test['html'])):
                        # Debugging
                        #print repr(normalize.normalize_html(compiler.to_html(test['markdown'])))
                        #print repr(normalize.normalize_html(test['html']))
                        fail = True
                except UnicodeDecodeError:
                    fail = True
                if fail:
                    errors[i] += 1
                    single_test_errors += 1
                    stdout_flush('F')
                else:
                    stdout_flush('.')
            times[i] += time.time() - start_time
        stdout_flush(' | ')
        stdout_flush('{} {} {} {} {}\n'.format(
            test['example'],
            test['start_line'],
            test['end_line'],
            single_test_errors,
            test['section'])
        )
    return total_tests, errors, times

def compiler_legend(compiler_ids):
    output = ''
    digits = order(len(compiler_ids))
    for i, name in enumerate(compiler_ids):
        if i != 0 and i % 5 == 0:
            output += '\n'
        output += '{:{}d} {}\n'.format(i + 1, digits, name)
    return output

if __name__ == '__main__':
    all_compiler_ids = Compilers.compiler_ids
    parser = argparse.ArgumentParser(
        description='Run CommonMark tests on multiple compilers.',
        epilog=r'''Most compilers only need to be available in the PATH to be uesed.
But we invite you to use the Vagrantfile setup
distributed with the soruce for greater reproductibility.

# Examples

Run all enabled and available tests with summarized error format:

    {f}

On the output:

- `.` indicates a passing test
- `F` indicates a failing test

Run all tests for the given compilers only:

    {f} multimarkdown pandoc

Run only tests whose section names match given regex filter:

    {f} -f string
    {f} -f string multimarkdown

# Enables vs Available

-   Enabled: compilers may be disabled through the file `{config_file}`.

-   Available: compilers are said to be available
    if they can be used if the user wishes.

    For command line utilies, this means that they are installed and in `PATH`.

    For REST APIs, this means that the internet connection and the server are working.

# No individual test output

This program does not run tests for individual compilers
and output the errors because CommonMark already does that well with:

    ./test/spec_test.py --program 'pandoc'

'''.format(f=sys.argv[0], config_file=config_file), # f contains command name.
        formatter_class=argparse.RawTextHelpFormatter, # Keep newlines.
    )
    parser.add_argument(
        '-a',
        '--enable-all',
        action='store_true',
        default=False,
        help='Enable all compilers for a single command.'
    )
    parser.add_argument(
        '-l',
        '--list-compilers',
        action='store_true',
        default=False,
        help='List compilers. Override all other options and nothing else is done.'
    )
    parser.add_argument(
        '-n',
        '--number',
        default=None,
        type=int,
        help='''Only run the test with given number.
The number of a test is affected by filtering options such as `-s`.'''
    )
    parser.add_argument(
        '-f',
        '--filter',
        default='',
        help='''Only run tests whose section name matches the given regex.'''
    )
    parser.add_argument(
        'compilers',
        choices=(all_compiler_ids + [[]]),
        nargs='*',
        help='''If given, only run tests for the given compilers even if they are disabled.
        Else, run all compilers which are both enabled and available.
        This option overrides -a'''
    )
    args = parser.parse_args()

    disabled_by_conf = config['run_all_disable']
    if args.compilers:
        enabled_compiler_ids = args.compilers
    else:
        if args.enable_all:
            enabled_compiler_ids = all_compiler_ids
        else:
            enabled_compiler_ids = \
                filter(lambda e: not e in disabled_by_conf, all_compiler_ids)
    enabled_and_available_compiler_ids = \
        filter(lambda e: getattr(Compilers, e).available(), enabled_compiler_ids)
    enabled_and_not_available_compiler_ids = \
        filter(lambda x: not x in enabled_and_available_compiler_ids,
                                  enabled_compiler_ids)

    if args.list_compilers:
        print 'All:                   {}\n' \
              'Enabled:               {}\n' \
              'Available:             {}\n' \
              'Enabled and Available: {}'.format(
              ', '.join(all_compiler_ids),
              ', '.join(enabled_compiler_ids),
              ', '.join(filter(lambda e: getattr(Compilers, e).available(),
                        all_compiler_ids)),
              ', '.join(enabled_and_available_compiler_ids),
        )
    else:
        if disabled_by_conf:
            print 'Disabled compilers:              {}'. \
                format(', '.join(disabled_by_conf))
            newline = True
        if enabled_and_not_available_compiler_ids:
            print 'Enabled compilers not available: {}'. \
                format(', '.join(enabled_and_not_available_compiler_ids))
            newline = True
        if newline:
            print
        if enabled_and_available_compiler_ids:
            compiler_legend = compiler_legend(enabled_and_available_compiler_ids)
            print compiler_legend
            compilers = [getattr(Compilers, compiler_name)
                         for compiler_name in enabled_and_available_compiler_ids]
            print 'Test results | Test number | Start line | End line | Failed tests | Section'
            print
            total_tests, errors, times = run_tests(spec_tests.get_tests(spec_path), compilers, args)
            print
            # print compiler_legend
            print 'Compiler id | Total time | Total errors | Error percent'
            print
            max_id_len = len(max(enabled_and_available_compiler_ids, key=len))
            for i, compiler in enumerate(compilers):
                if total_tests == 0:
                    percent = 0
                else:
                    percent = int(errors[i]/float(total_tests)*100)
                    print '{:<{}} {:>8.4f}s {:>4} {:>3}%'.format(
                        enabled_and_available_compiler_ids[i],
                        max_id_len,
                        times[i],
                        errors[i],
                        percent
                    )
        else:
            print 'No compilers are enabled. Install or enable some.'
