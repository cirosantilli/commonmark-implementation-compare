#!/usr/bin/env bash
set -ev

bin_dir='/usr/local/bin'

## Dependencies

  sudo apt-get update
  sudo apt-get install -y build-essential bison cmake curl git haskell-platform lua5.1 libglib2.0-dev mercurial unzip

  # go
  # Requires: mercurial, bison.
  if [ ! -f "$HOME/.gvm/scripts/gvm" ]; then
    bash < <(curl -LSs 'https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer')
  fi
  . "$HOME/.gvm/scripts/gvm"
  gvm install 'go1.2.2'
  gvm use 'go1.2.2' --default

  # haskell
  printf '\n%s\n' 'export PATH="$PATH:$HOME/.cabal/bin"' >> "$HOME/.profile"
  cabal update

  # nodejs
  VERSION='0.10.26'
  curl 'https://raw.githubusercontent.com/creationix/nvm/v0.7.0/install.sh' | sh
  . "$HOME/.nvm/nvm.sh"
  echo '. "$HOME/.nvm/nvm.sh"
  nvm use "'"$VERSION"'" &>/dev/null
  ' >> "$HOME/.bashrc"
  nvm install "$VERSION"

  # python pip
  wget -O- https://bootstrap.pypa.io/get-pip.py | sudo python

  # ruby
  # https://github.com/wayneeseguin/rvm
  # blocked by https://github.com/wayneeseguin/rvm/issues/3110
  gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
  curl -L https://get.rvm.io | bash -s stable
  . "$HOME/.rvm/scripts/rvm"
  rvm install 2.1.1

## Engines

  # blackfriday
  # TODO: use latest stable version.
  go get 'github.com/russross/blackfriday'
  go get 'github.com/russross/blackfriday-tool'

  # cmark
  dir='cmark'
  cd '/tmp'
  git clone 'https://github.com/jgm/CommonMark' "$dir"
  cd "$dir"
  git checkout "$(git describe --tags --abbrev=0)"
  make
  sudo mv 'build/src/cmark' "$bin_dir"
  cd '..'
  rm -rf -- "$dir"

  # commonmark.js
  # https://github.com/jgm/CommonMark
  npm install -g 'commonmark'


  # CommonMark-py
  # https://github.com/rolandshoemaker/CommonMark-py
  sudo pip install commonmark

  # hoedown
  # https://github.com/hoedown/hoedown
  dir='hoedown'
  cd '/tmp'
  git clone 'https://github.com/hoedown/hoedown' "$dir"
  cd "$dir"
  git checkout "$(git describe --tags --abbrev=0)"
  make
  sudo mv 'hoedown' "$bin_dir"
  cd '..'
  rm -rf -- "$dir"

  # kramdown
  # https://github.com/gettalong/kramdown
  gem install 'kramdown'

  # lunamark
  # TODO get working. 'alt_getopt' not found.
  #dir='lunamark'
  #cd '/tmp'
  #git clone 'https://github.com/jgm/lunamark' "$dir"
  #cd "$dir"
  ## TODO use latests stable version.
  ##git checkout "$(git describe --tags --abbrev=0)"
  #make standalone
  #sudo mv 'lunamark' "$bin_dir"
  #cd '..'
  #rm -rf -- "$dir"

  # markdwn_pl
  # http://daringfireball.net/projects/markdown/
  dir='Markdown_1.0.1'
  zip="${dir}.zip"
  cd '/tmp'
  wget -O "${zip}" 'http://daringfireball.net/projects/downloads/Markdown_1.0.1.zip'
  unzip "${zip}"
  sudo mv "${dir}/Markdown.pl" "$bin_dir"
  rm -rf -- "$dir" "$zip"

  # markdown2
  # https://github.com/trentm/python-markdown2
  sudo pip install 'markdown2'

  # marked
  # https://github.com/chjj/marked
  npm install -g 'marked'

  # maruku
  # https://github.com/bhollis/maruku
  gem install 'maruku'

  # markdownjs
  # https://github.com/evilstreak/markdown-js
  npm install -g 'markdown'

  # multimarkdown
  # https://github.com/fletcher/MultiMarkdown-4
  dir='MultiMarkdown-4'
  cd '/tmp'
  git clone --recursive 'https://github.com/fletcher/MultiMarkdown-4' "$dir"
  cd "$dir"
  git checkout "$(git describe --tags --abbrev=0)"
  make
  sudo make install
  cd '..'
  rm -rf -- "$dir"

  # pandoc
  # https://github.com/jgm/pandoc
  # TODO: 1Gb memory is not enough, on 2Gb it made my host halt.
  #cabal install 'pandoc'

  # peg-markdown
  # https://github.com/jgm/peg-markdown
  # Requires: libglib2.0-dev.
  dir='peg-markdown'
  cd '/tmp'
  git clone 'https://github.com/jgm/peg-markdown' "$dir"
  cd "$dir"
  git checkout "$(git describe --tags --abbrev=0)"
  make
  sudo mv 'markdown' "${bin_dir}/peg-markdown"
  cd '..'
  rm -rf -- "$dir"

  # rdiscount
  # https://github.com/davidfstr/rdiscount
  gem install 'rdiscount'

  # redcarpet
  # https://github.com/vmg/redcarpet
  gem install 'redcarpet'

  # showdown
  # https://github.com/showdownjs/showdown
  npm install 'showdown'
  # TODO the ideal global install is not working. Why?
  #npm install -g 'showdown'

# Required or else Karmdown and Maruku raise UTF-8 exceptions.
# with the default `LC_ALL=en_US`.
printf '\n%s\n' 'export LC_ALL=""' >> "$HOME/.profile"

printf '\n%s\n' 'cd /vagrant' >> "$HOME/.bashrc"
