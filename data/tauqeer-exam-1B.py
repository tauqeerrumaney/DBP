#!/usr/bin/env python3
#tried using importing argparser, but couldn't get output so used system arguments even tho size is greater than 3
import sys, os, re, gzip

def seqStart(filename, uid = ''):
    
    if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
    else:
            file = open(filename,'rt')
    
    ID = '^ID\s+'+uid
    dc = {}
    flag = False
    sid=''
    seq=''
    for line in file: 
        if re.search(ID,line):
            sid = line.split()[1]
        elif re.search('^SQ\s',line):
            flag = True
        elif flag and '//' not in line:
            seq = line.split()[0]
            flag= False
            dc.update({sid:seq})
    return(dc)

def usage ():
    print('''--help|tauqeer-exam-1B.py filename --seq-start   UID  
Uniprot-Parser by Tauqeer Kasam Rumaney, 2022
Extract information from Uniprot data files.
-------------------------------------------
Mandatory arguments are:
 FILE - one or more compressed or uncompressed Uniprot data files
 --help - display this help page
 --seq-start - show the first then amino acids for all or only for the given
 UniProt ID
 UID - a valid UniProt ID like AP3A_SARS2''')                  
                
def main(argv):
    if len(argv)<4 or sys.argv[0] == "--help":
        usage()
    else: 
        if sys.argv[2]== "--seq-start":
            dc=seqStart(argv[1],argv[3])
            print(dc)
        
        else:
            print(f"Error: Valid options are: --help filename --seq-start  UID") 
                        
 ## check for main script
if "__main__" == __name__:
    main(sys.argv)
