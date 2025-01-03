#!/usr/bin/env python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

text = text.split('\n') #Separate each line
for i in range (len(text)): #Loop to put a star before each line
    text[i]="* " + text[i]
text = '\n'.join(text)


pyperclip.copy(text)