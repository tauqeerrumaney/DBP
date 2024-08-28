#!/usr/bin/env python3
# by YSD 

import sys, os, re, gzip

def usage ():
    print('''ABC-exam-1.py --help|--seq-start|--get-entry [FILE] ?[UPID]?
Uniprot-Parser by Maxi Yiu, 2022
Extract information from Uniprot data files.
-------------------------------------------
Mandatory arguments are:
 FILE - one or more compressed or uncompressed Uniprot data files
Optional arguments are (either --help or --seqstart must be given):
 --help - display this help page
 --seq-start - show the first then amino acids for all or only for the given
 UniProt ID
 --get-entry - show the Uniprot entry for the given UniProt ID (not implemented)
 
 UPID - a valid UniProt ID like AP3A_SARS2''')

def seqStart(filename, uid = ''):
    
    if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
    else:
            file = open(filename,'r')
    
    ID = '^ID\s+'+uid
    dc = {}
    
    for line in file: 
        if re.search(ID,line):
            sid = line.split()[1]
            print(sid)
            dc[sid] = []
        
    exit()
                  
def checkFileID(x,y=''):
    if '.' in x:
        filename, uid = x,y
    else:
        filename, uid = y,x
        
    if re.search('.+gz$',filename) or re.search('.dat$',filename):
        filename = os.getcwd()+'/'+filename
        if not(os.path.exists(filename)) :
            print(f"Error {filename} doesn't exist")
            exit()    
    else:
        print(f"Error {filename} is not a gz or dat format")
        exit()
    
    if uid != '' and (re.search("[^A-Z_0-9]",uid)):
        print(f"Error UPID:{uid} is not valid ")
        exit()
    
    return (filename,uid)
                
def main(args):
    if len(args)<2 or '--help' in args:
        usage()
    else: 
        if args[1] == '--seq-start' and len(args) > 2:
            if len(args) == 4:
                filename, uid = checkFileID(args[2],args[3])
            else:
                filename, uid = checkFileID(args[2])
            
            seqStart(filename,uid)
        
        else:
            print(f"Error: Valid options are: --seq-start [filename | UPID ]| --help") 
                        
 ## check for main scrip
if "__main__" == __name__:
    main(sys.argv)
