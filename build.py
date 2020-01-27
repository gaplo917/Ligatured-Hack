#!/usr/bin/env python
import sys
from glob import glob
from ligaturize import ligaturize_font

# Rebuild script for ligaturized fonts.
# Uses ligaturize.py to do the heavy lifting; this file basically just contains
# the mapping from input font paths to output fonts.

# For the prefixed_fonts below, what word do we stick in front of the font name?
LIGATURIZED_FONT_NAME_SUFFIX = 'Ligatured'

# Should we copy some individual punctuations characters like &, ~, and <>,
# as well as ligatures? The full list is in ligatures.py.
COPY_CHARACTER_GLYPHS = False

# If copying individual characters, how different in width (relative to the font
# we're ligaturizing) should they be before we attempt to width-correct them?
# The default (0.1) means to width-correct if they're +/- 10%. Values >1.0
# effectively disable this feature.
SCALE_CHARACTER_GLYPHS_THRESHOLD = 0.1

# Fonts that will be ligaturized. ####
# Don't put fonts licensed under UFL here, and don't put fonts licensed under
# SIL OFL here either unless they haven't specified a Reserved Font Name.

input_fonts = [
  'fonts/hack/build/ttf/*.ttf'
]

# No user serviceable parts below this line. ####

for pattern in input_fonts:
  files = glob(pattern)
  if not files:
    print("Error: pattern '%s' didn't match any files." % pattern)
    sys.exit(1)
  for input_file in files:
    ligaturize_font(
      input_font_file=input_file,
      ligature_font_file=None,
      output_dir='fonts/output/',
      suffix=LIGATURIZED_FONT_NAME_SUFFIX,
      output_name=None,
      copy_character_glyphs=COPY_CHARACTER_GLYPHS,
      scale_character_glyphs_threshold=SCALE_CHARACTER_GLYPHS_THRESHOLD
    )
