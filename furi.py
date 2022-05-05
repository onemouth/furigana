#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title furi
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "kanji" }
# @raycast.argument2 { "type": "text", "placeholder": "furigana" }
# @raycast.packageName furigana

# Documentation:
# @raycast.description generate html ruby snippets
# @raycast.author onemouth

import sys
import subprocess

s = f"<ruby>{sys.argv[1]} <rt>{sys.argv[2]}</rt></ruby>"
subprocess.run("pbcopy",
               env={'LANG': 'en_US.UTF-8'},
               universal_newlines=True,
               input=s,
               encoding='utf-8')

print(s)
