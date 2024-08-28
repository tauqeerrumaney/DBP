#!/usr/bin/env python3
## templates/PyApp.py

import sys, os, re
import gzip
class UniProtTool:
    def getEntry (self,filename,uid=""):
        if re.search(".+gz$",filename):
            file = gzip.open(filename, "rt")
        else:
            file = open(filename, "t")
        flag=False
        res=""
        for line in file:
            if re.search("^ID\s+"+uid,line):
                flag=True
                res=line
            elif flag and re.search("^ID",line):
                break
            elif flag:
                res=res+line
       
        file.close()
        return res

    def seqstart(self,filename,uid=""):
        entry=self.getEntry(filename,uid)
        flag = False
        res = ""
        print("abc")
        for line in entry.split("\n"):
            if re.search("^SQ\s+" + uid, line):
                flag = True
                print("123")
                res = line
            elif flag and re.search("^//", line):
                break
            elif flag:
                res = res + line + "\n"
        print("xyz")
        return (res)
        
def usage(argv):
        print("Usage: %s uni-prot file seqstart uni-prot id" % args[0])

def main(argv):
        if len(argv) < 4:
            usage(sys.argv)
        else:
            up=UniProtTool()
            if argv[2]== "seqstart":
                res=up.seqstart(argv[1],argv[3])
            else:
                print("Error")
                usage(sys.argv)
            print(res,end="")

if "__main__" == __name__:
        main(sys.argv)
