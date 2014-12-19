#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import difflib
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
        shell  = False,
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True
    )
    stdout, stderr = process.communicate(stdin)
    exit_status = process.wait()
    if exit_status != 0:
        raise Exception('Command exit status was not 0.')
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

    # List of all the compiler classes. TODO DRY this up and look them up with instrospection.
    compiler_ids = [
        'gfm',
        'blackfriday',
        'hoedown',
        'kramdown',
        'lunamark',
        'markdown2',
        'markdown_pl',
        'marked',
        'maruku',
        'md2html',
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
        <http://developer.github.com/v3/#rate-limiting>
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
    class hoedown(CommandCompiler): command = ['hoedown']
    class kramdown(CommandCompiler): command = ['kramdown']
    class lunamark(CommandCompiler): command = ['lunamark']
    class markdown2(CommandCompiler): command = ['markdown2']
    class markdown_pl(CommandCompiler): command = ['Markdown.pl']
    class marked(CommandCompiler): command = ['marked']
    class maruku(CommandCompiler): command = ['maruku']
    class md2html(CommandCompiler): command = ['md2html']
    class multimarkdown(CommandCompiler): command = ['multimarkdown']
    class pandoc(CommandCompiler): command = ['pandoc']
    class peg_markdown(CommandCompiler): command = ['peg-markdown']
    class rdiscount(CommandCompiler): command = ['rdiscount']
    class redcarpet(CommandCompiler): command = ['redcarpet']
    class showdown(CommandCompiler): command = ['node', 'showdown-stdin.js']

def stdout_flush(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def run_tests(tests, compilers, args):
    total_compilers = len(compilers)
    errors = [0] * total_compilers
    times = [0.0] * total_compilers
    tests = itertools.ifilter(lambda test: re.match(args.filter,
                              test['section']), tests)
    tests = list(tests)[:5]
    for test in tests:
        for i, compiler in enumerate(compilers):
            start_time = time.time()
            if not args.number or total == args.number:
                if (normalize.normalize_html(compiler.to_html(test['markdown'])) ==
                    normalize.normalize_html(test['html'])):
                    stdout_flush('.')
                else:
                    errors[i] += 1
                    stdout_flush('F')
            if i % 5 == 4:
                stdout_flush('  ')
            times[i] += time.time() - start_time
        stdout_flush(' | ')
        stdout_flush('{} {} {} {}\n'.format(test['example'], test['start_line'],
                                            test['end_line'], test['section']))
    return len(tests), errors, times

def compiler_legend(compiler_ids):
    output = ''
    digits = order(len(compiler_ids))
    for i, name in enumerate(compiler_ids):
        output += '{:{}d} {}\n'.format(i + 1, digits, name)
        if i % 5 == 4:
            output += '\n'
    return output

if __name__ == '__main__':
    all_compiler_ids = Compilers.compiler_ids
    parser = argparse.ArgumentParser(
        description='Run markdown tests.',
        epilog=r'''# Examples

Run all enabled and available tests with summarized error format:

    {f}

Each summary output line is of the form:

    multimarkdown |.F..|   0.60s  4   1  25%

Where:

- `.` indicates a passing test
- `F` indicates a failing test
- `0.60s` is the wall time used to run all commands
- `4` is the total number of tests
- `1` is the total number of failing tests
- `25%` is the percentage of failing tests

Run all tests for the given compiler:

    {f} multimarkdown

Run only tests whose section names match given regex filter:

    {f} -p string
    {f} -p string multimarkdown

# Definitions

-   enabled: compilers may be disabled through the file `{config_file}`.

-   available: compilers are said to be available
    if they can be used if the user wishes.

    For command line utilies, this means that they are installed and in `PATH`.

    For REST APIs, this means that the internet connection and the server are working.

# Normalization

In order for output comparison to be meaningful, HTML outputs must be normalized
before comparison.

The chosen normalization is heuristic, and goes beyond simple DOM tree transformation:
its goal is to normalize outputs that render equally in most browsers as equal,
and different DOM trees may render exactly the same on most browsers.

Normalized aspects include:

- convert multiple consecutive whitespaces to a single space
- sort attributes alphabetically
- remove attributes such as `id` or `class` which are added by many compilers
- self-closing tags are transformed into regular tags, as they are equivalent in HTML5
- references are converted to Unicode
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
    # TODO allow this to take multiple arguments.
    # Single argument is useless as spec_test.py can be used directly.
    #parser.add_argument(
        #'compiler',
        #choices=all_compiler_ids,
        #nargs='?',
        #help='''If given, only run tests for this compiler even is disabled,
        #and print actual / expected IO for each failing test.
        #Else, run all compilers which are both enabled and available,
        #and print only summarized output.'''
    #)
    args = parser.parse_args()

    disabled_by_conf = config['run_all_disable']
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
            total_tests, errors, times = run_tests(spec_tests.get_tests(spec_path), compilers, args)
            print
            print compiler_legend
            print 'Total tests: ' + str(total_tests)
            print
            print 'Total time / Total errors / Error percent'
            digits = order(len(enabled_and_available_compiler_ids))
            for i, compiler in enumerate(compilers):
                if total_tests == 0:
                    percent = 0
                else:
                    percent = int(errors[i]/float(total_tests)*100)
                    print '{:{}d} {:>.4f}s {} {}%'.format(i + 1, digits, times[i], errors[i], percent)
        else:
            print 'No compilers are enabled. Install or enable some.'
