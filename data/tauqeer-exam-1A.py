#!/usr/bin/env python3
#tried using importing argparser, but couldn't get output so used system arguments even tho size is greater than 3
import sys, os, re, gzip, argparse

class Uniprot:
    def __init__(self):
        pass
    
    def getentry(self,filename,uid):
        if '.' in filename:
            filename, uid = filename,uid
        else:
            filename, uid = uid,filename
        #since we are on the same directory, we are using ^uniprot_sprout_, if not in sme directory, we shouldn't use ^ symbol
        if re.search("^uniprot_sprot_",filename):
            print("File exist")
            if re.search(".+gz$",filename):
                file = gzip.open(filename, "rt")
            else:
                file = open(filename, "rt")
            flag=True
            for line in file:
                if re.search("^ID\s+"+uid,line):
                    print("All fine but no functionality yet")
                    break
                else:
                    flag=False
            if flag==False:
                print("Invalid UniProt ID")
        else:
            print("File", filename ,"does not exist")


def usage(argv):
    print("""--help | tauqeer-exam-1.py [FILE] ? --get-entry [UPID]?
Uniprot-Parser by Tauqeer Kasam Rumaney, 2022
Extract information from Uniprot data files.
-------------------------------------------
Mandatory arguments are:
 FILE - one or more compressed or uncompressed Uniprot data files
 --help - display this help page
 --get-entry - show the Uniprot entry for the given UniProt ID (not implemented)

 UPID - a valid UniProt ID like AP3A_SARS2""")
 
def main(argv):
    upt = Uniprot()
    
    if len(sys.argv)<4 or sys.argv[0] == "--help":
        usage(argv)
    else:
        if sys.argv[2]== "--get-entry":
            upt.getentry(argv[1],argv[3])
        else:
            print(f"Error: Valid options are:--help filename --get-entry  UID ") 

    

 ## check for main script
if __name__ == '__main__':
    main(sys.argv)
