#!/usr/bin/env python3
 ## templates/PyApp.py
import sys, os, re

def usage ():
    print("Usage: app.py arg1 [arg2]")
    
    
def main(args):
    if len(args) < 2:
        usage()
    else:
        print("main is running")

 ## check for main script
if "__main__" == __name__:
    main(sys.argv)
