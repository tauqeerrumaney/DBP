#!/usr/bin/env python3
import sys,os

def usage():
    print("Appname by Author, Uni Potsdam, 2022")
    print("Usage: appname --arg value")
    exit()


def wc (filename):
    nlines = 0
    nwords = 0
    nchars = 0
    nlow   = 0
    nupp   = 0
    file= open(filename,"r")
    for line in file:
        nlines = nlines + 1
        nwords = nwords + len(line)
        nchars = nchars + len(line.split())
    file.close()
    return(tuple((nlines,nwords,nchars,nlow, nupp, filename)))

def main(args):
    if len(args) == 1 or "-h" in args:
        usage()
    elif len(args) > 1 and "-l" in args:
        res= xyz(sys.argv[2])
        print("%i\t%s" % (res[0],res[5]))
    else:
        print(xyz(sys.argv[1]))

if __name__ == "__main__":
    main(sys.argv)
