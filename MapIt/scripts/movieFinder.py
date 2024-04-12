#! Python3
# movieFinder.py- loads an fmovies web page to a movie using input from the
# command line or clipboard

import sys, pyperclip, webbrowser

if __name__ == "__main__":

    commandLineInput  = sys.argv[1:]
    clipBoardInput = pyperclip.paste()

    if commandLineInput:
        movie = " ".join(commandLineInput)
    else:
        movie = clipBoardInput

    webbrowser.open(f"https://fmoviesz.to/filter?keyword={movie}")