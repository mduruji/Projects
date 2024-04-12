#! python3
# mapit.py- Launches a map in the browser using an address from
# the command line or clipboard

import sys, pyperclip, webbrowser

# check if there was input in the command line
if len(sys.argv) > 1:
    # create the string bases on the input
    address = ' '.join(sys.argv[1:])
else:
    # if no  input paste from the clipboard
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')