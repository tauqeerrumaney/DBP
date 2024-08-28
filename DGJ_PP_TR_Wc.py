#!/usr/bin/env python3
#Dhvaniben Ghanshyambhai Jasoliya
#Poojitha Ponnam
#Tauqeer Rumanay
import re

def wc (filename):
    nlines = 0
    nwords = 0
    nchars = 0
    nspaces = 0
    nlow   = 0
    nupp   = 0
    # open file in read mode
    # go over every line
    # increment nlines by one
    with open(filename, 'r') as f:
        for line in f:
            nlines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    nwords += 1
                    word = 'N'
                elif (letter == ' '):
                    nspaces += 1
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        nchars += 1
        f.seek(0)
        file=f.read()
        nupp=len(re.sub("[^A-Z]+","",file))
        nlow=len(re.sub("[^a-z]+","",file))
        f.close()
    return(tuple((nlines,nwords,nchars,nlow, nupp, filename)))   

# use our Python file for testing
print(wc("result.txt"))