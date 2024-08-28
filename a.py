#!/usr/bin/env python3
## templates/PyApp.py
import sys, os, re

def usage ():
    us = "tkr_parser1.py --help|--go|--doi [FILE] ?[FILE] ...?"
    print(us)

def help():
    string = """Usage: tkr_parser.py --help|--go|--doi [FILE] ?[FILE] ...?
Uniprot-Parser by TKR, 2023
Extract information from Uniprot data files.
-------------------------------------------
Optional arguments are:
    --help - display this help page
    --go   - show a protein id to GO id mapping
    --doi  - show a protein id to DOI mapping (not used today)
Mandatory arguments are:
    FILE - one or more compressed or uncompressed Uniprot data files"""    
    print(string)
    exit()
    
def checkInps(args):
    cmd = args[1]
    files = args[2:]
    valid_cmds = ['--go','--doi']
    valid_exts = ['.dat','.gz']
    
    if cmd not in valid_cmds:
        usage()
        print(print(f"Unknown option {args[1]}, valid options are {' '.join(valid_cmds)}"))
        exit()
        
    for fname in files:
        filepath = os.getcwd() + "/" +fname
        if not(re.search(f'.dat$',fname)) and not(re.search(f'.gz$',fname)):
            usage()
            print(f"Error: {fname} should have an extension of {' '.join(valid_exts)}")   
            exit()

        if not(os.path.exists(filepath)):
            usage()
            print(f"Error: {fname} doesn't exist kindly re-enter the file names")
            exit()
    return True

def resultPrinter(dc,cmd):
    print("Everything is fine but no functionality")

def main(args):
    if '--help' in args:
        help()
    elif len(args) <= 2:
        usage()
    else:
        valid = checkInps(args)
        if valid:
            cmd = args[1]
            dc = {}
            resultPrinter(dc,cmd)

## check for main script
if "__main__" == __name__:
    main(sys.argv)
