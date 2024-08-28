#!/usr/bin/env python3

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
 
 UID - a valid UniProt ID like AP3A_SARS2''')

def seqStart(filename, uid = ''):
    if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
    else:
            file = open(filename,'rt')
    
    ID = '^ID\s+'+uid
    dc = {}
    seq_started = False
    flag = False
    sid = ''
    seq = ''
    for line in file: 
        if re.search(ID,line):
            sid = line.split()[1]
            dc[sid] = []
            flag = True
        
        elif flag and re.search('^SQ\s',line):
           seq_started = True 
        
        elif seq_started and '//' not in line:
            seq = line.split()[0]
            dc[sid].append(seq)
            seq_started = False
            flag = False
        
    return (dc)
                  
def checkFileID(file,sid=''):
    if '.' in file:
        filename, uid = file,sid
    else:
        filename, uid = sid,file
        
    if re.search('.+gz$',filename) or re.search('.dat$',filename):
        filename = os.getcwd()+'/'+filename
        if not(os.path.exists(filename)) :
            print(f"Error {filename} doesn't exist")
            exit()    
    else:
        print(f"Error {filename} is not a gz or dat format")
        exit()
    
    if uid != '' and (re.search("[^A-Z_0-9]",uid)):
        print(f"Error UID:{uid} is not valid ")
        exit()
    
    return (filename,uid)

def printIDAmino(dc):
    for key,value in dc.items():
        print(f"{key} \t {value}")
     
def main(args):
    if len(args)<2 or '--help' in args:
        usage()
    else: 
        if args[1] == '--seq-start' and len(args) > 2:
            if len(args) == 4:
                filename, uid = checkFileID(args[2],args[3])
            else:
                filename, uid = checkFileID(args[2])
            
            dc = seqStart(filename,uid)
            printIDAmino(dc)
        
        else:
            print(f"Error: Valid options are: --seq-start [filename | UPID ]| --help") 
                        
 ## check for main scrip
if "__main__" == __name__:
    main(sys.argv)