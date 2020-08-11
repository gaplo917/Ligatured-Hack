#!/bin/sh

# Use this method to get the font, because the git submodule of nerd font is too big!
NERD_TAG=$(curl https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest | jq -r .tag_name);
curl "https://github.com/ryanoasis/nerd-fonts/releases/download/${NERD_TAG}/Hack.zip" -L -o fonts/nerd-fonts/Hack.zip
unzip -o fonts/nerd-fonts/Hack.zip -d fonts/nerd-fonts/
rm -f fonts/nerd-fonts/Hack.zip
