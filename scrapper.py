import sys
from visualMajor import visual
from scrapperMajor import headless
from os import path, mkdir


command = sys.argv
if len(command) > 1:
    if command[1] == "visual":
        if path.exists('data'):
            print('Already Exists...')
        else:
            mkdir('data')
            print('No data directory found.')
            print('Creating Directory...')
        visual()
    elif command[1] == "headless":
        if path.exists('data'):
            print('Already Exists...')
        else:
            mkdir('data')
            print('No data directory found.')
            print('Creating Directory...')
        headless()
    elif command[1] == "help":
        print("""
Usage: python3 scrapper.py [arguments]
Arguments:
    visual - To view scrapping result both commandline and in browser
    headless - To view scrapping result in commandline only
    help - To view this help pompt""")
else:
    print("Error: No argument provided or invalid argument.")
    print("""
Usage: python3 scrapper.py [arguments]
Arguments:
    visualScrapper - To view scrapping result both commandline and in browser
    commandLineScrapper - To view scrapping result in commandline only
    help - To view this help pompt""")
