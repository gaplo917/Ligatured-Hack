# Ligatured Hack
[![Build Status](https://travis-ci.com/gaplo917/Ligatured-Hack.svg?branch=master)](https://travis-ci.com/gaplo917/Ligatured-Hack)

This project is forked from [Ligaturizer@daa4dc8b](https://github.com/ToxicFrog/Ligaturizer/tree/daa4dc8baffeefcb27c4ffd30ea52797ead8d123) 
which is [not able to build latest Hack 3.x font](https://github.com/ToxicFrog/Ligaturizer/issues/73) at that moment

I created a [fix](https://github.com/gaplo917/Ligaturizer/commit/cc5ae602f8b861a640220997092abf06dcea6ea5) and submitted 
a [pull request](https://github.com/ToxicFrog/Ligaturizer/pull/81). This fix is compatible to build all fonts originally listed on Ligaturizer. 
However, it is too difficult for me to manually check all the output fonts.

To make this project more maintainable. I decided to 
* focus only on Ligatured Hack Font (My Favourite Font) 
* containerize dependencies (Reproducible, hopefully OS independent)
* create automatic CI/CD. (Hassle free update)

> Thus, splitting out is unavoidable.

# Current Status
|Task|Status|
|:-----:|:-----:|
|Containerize fontforge and python runtime| ✅ |
|Travis CI to build release| ✅ |
|Build Automatically upon FIRA or Hack update hook | WIP |

# Download Ligatured Hack Fonts
Go to [release](https://github.com/gaplo917/Ligatured-Hack/releases)


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
