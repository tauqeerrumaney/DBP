#TKR_PP_UHV_RBP
#!/usr/bin/env python3
## templates/PyApp.py
import sys, os, re
import gzip
class UniProtTool:
    def __init__(self):
        pass
    def getEntry (self,filename,uid=""):
        if re.search(".+gz$",filename):
            file = gzip.open(filename, "rt")
        else:
            file = open(filename, "rt")
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

    def getSeq(self,filename,uid=""):
        entry=self.getEntry(filename,uid)
        flag = False
        res = ""
        for line in entry.split("\n"):
            if re.search("^SQ\s",line):
                flag = True
                res = line + "\n"
            elif flag and re.search("^//", line):
                break
            elif flag:
                res = res + line + "\n"
        return (res)

    def getFasta(self, filename, uid):
        seq = self.getSeq(filename, uid)
        # seq=uid+seq.replace(" ","")
        # lmt = [seq.split("\n")]
        # for  in seq:
        #     if re.search(';[^;]*$'):
        #         seq1=i
        #         else
        #         seq2 = i
        lmt=[seq.split("\n")]
        seq1 = lmt[0][0]
        seq2= str(lmt[0][1:])
        seq = uid+seq1+seq2.replace(" ","")
        # k = []
        # print(lmt)
        # print(lmt[0][0])
        # for i in seq2:
        #         k= i.replace(" ","")
        # print(k)
        return (seq)

def usage(args):
        print("Usage: %s uni-prot file getEntry|getSeq uni-prot id" % args[0])

def main(args):
        if len(args) < 4:
            usage(sys.argv)
        else:
            #print("main is running")
            up=UniProtTool()
            if args[2]== "getFasta":
                res=up.getSeq(args[1],args[3])
                print(res, end="")
            elif args[2]== "getEntry":
                res = up.getEntry(args[1], args[3])
                print(res, end="")
            else:
                print("Error")
                usage(sys.argv)


    ## check for main script
if "__main__" == __name__:
        main(sys.argv)
