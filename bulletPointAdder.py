#! python3

# Programmer:  Matthew Landes
# Date:		   March 22, 2020
# Book:		   Automate The Boring Stuff with Python
# Project:     Chapter 6 Project - Adding Bullets to Wiki Markup
# Description: bulletPointAdder.py - Adds Wikipedia bullet points to the startswith
#              of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
