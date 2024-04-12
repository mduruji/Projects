#! Python3
# bookSearch- opens an amazon page of a book using input from the
# command line or clipboard

import sys, webbrowser, pyperclip

if __name__ == "__main__":

    commandLineInput  = sys.argv[1:]
    clipBoardInput = pyperclip.paste()

    # check if user provided an input
    if commandLineInput:
        # instantiate var product to the command line input
        product = " ".join(commandLineInput)
    else:
        product = clipBoardInput

    webbrowser.open(f"https://www.amazon.com/s?k={product}")