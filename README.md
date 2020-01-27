# Ligatured Hack
[![Build Status](https://travis-ci.com/gaplo917/Ligatured-Hack.svg?branch=master)](https://travis-ci.com/gaplo917/Ligatured-Hack)
[![GitHub release](https://img.shields.io/github/v/release/gaplo917/Ligatured-Hack.svg)](https://gitHub.com/gaplo917/Ligatured-Hack/releases/)

I love Hack font and ligatures and can't wait to get latest release. 

That's why I build this project with fully automated CI/CD.

|Task|Status|
|-------|:-------:|
|Focus only Hack Font|✅|
|Containerize fontforge and python runtime (Reproducible)|✅|
|Automactically Build from Travis CI (Hassle-free)|✅|
|Automactically Build if Hack/Fira has new release (Daily Cron)|✅|

Yes! You could ***star*** this repo and ***watch*** the release channel to get the latest Hack & Fira Ligatured Font updates!

If you also have a favourite font want to ligaturize, you can ***fork*** this repo and make corresponding changes on git submodules & travis ci settings, you will benefit from getting hassle free updates of your favourit font!

# Project History
This repository is forked from [Ligaturizer@daa4dc8b](https://github.com/ToxicFrog/Ligaturizer/tree/daa4dc8baffeefcb27c4ffd30ea52797ead8d123). 

At that moment, Ligaturizer was [not able to build latest Hack 3.x font](https://github.com/ToxicFrog/Ligaturizer/issues/73). I submitted 
a [pull request](https://github.com/ToxicFrog/Ligaturizer/pull/81) to fix that issue. 

However,
* it is too difficult for me to manually check all the output fonts' correctness.
* Too many fonts that I don't use
* No container, No automatic CI/CD


# Download Ligatured Hack Fonts
Go to [release](https://github.com/gaplo917/Ligatured-Hack/releases)

For intelliJ with **window 10** users, you have to right click the fonts and choose 'install fonts for all users' in order to be listed in intelliJ. 

For **Mac** users who want to upgrade 'Hack Ligatured' version, you are recommended to completely remove 'Hack Ligatured' in FontBook and install it again. 

# Manual 
```
# Clone
git clone https://github.com/gaplo917/Ligatured-Hack
cd Ligatured-Hack

# Update Fira, Hack submodules
git submodule update --depth 1 --init --recursive
```

### Manual Build via docker
```
# Build docker image
docker build . -t ligatured-hack

# Mount the volume & Run
docker run -v $(pwd)/fonts/output:/usr/src/app/fonts/output ligatured-hack
```

Done! All the fonts will be built to `$(pwd)/fonts/output`

### Manual Build via MacOS
```
# Install fontforge dependencies
brew install fontforge

# Run Makefile
make
```

# Credits
This script was originally written by [IlyaSkriblovsky](https://github.com/IlyaSkriblovsky) for adding ligatures to DejaVuSans Mono ([dv-code-font](https://github.com/IlyaSkriblovsky/dv-code-font)). [Navid Rojiani](https://github.com/rojiani) made a few changes to generalize the script so that it works for any font. [ToxicFrog](https://github.com/ToxicFrog) has made a large number of contributions.
