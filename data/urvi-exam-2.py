#!/usr/bin/env python3

import sys, os, re, gzip

def usage ():
    print('''task2_test1.py --help|--seq-start [FILE] ?[UPID]?
Uniprot-Parser by Urvi Hemant Virkar, 2022
Extract information from Uniprot data files.
-------------------------------------------
Mandatory arguments are:
 FILE - one or more compressed or uncompressed Uniprot data files
Optional arguments are (either --help or --seqstart must be given):
 --help - display this help page
 --seq-start - show the first then amino acids for all or only for the given
 UniProt ID
 UID - a valid UniProt ID like AP3A_SARS2''')

def seqStart(filename, uid = ''):
    
    if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
    else:
            file = open(filename,'rt')
    
    ID = '^ID\s+'+uid
    dictt = {}
    flag = False
    SID=''
    seq=''
    for line in file: 
        if re.search(ID,line):
            SID = line.split()[1]
        elif re.search('^SQ\s',line):
            flag = True
        elif flag and '//' not in line:
            seq = line.split()[0]
            flag= False
            dictt.update({SID:seq})
    return(dictt)
                  
def checkFileID(file,SID=''):
    if '.' in file:
        filename, uid = file,SID
    else:
        filename, uid = file,SID
        
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
                
def main(args):
    if len(args)<2 or '--help' in args:
        usage()
    else: 
        if args[1] == '--seq-start' and len(args) > 2:
            if len(args) == 4:
                filename, uid = checkFileID(args[2],args[3])
            else:
                filename, uid = checkFileID(args[2])
            
            dc=seqStart(filename,uid)
            print(dc)
        
        else:
            print(f"Error: Valid options are: --seq-start [filename | UID ]| --help") 
                        
 ## check for main script
if "__main__" == __name__:
    main(sys.argv)