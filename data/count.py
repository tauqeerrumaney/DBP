#Tauqeer Kasam Rumaney
#!/usr/bin/env python3
import sys, os, re, gzip

def seqCount(filename):
    global x
    if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
    else:
            file = open(filename,'rt')

    dc = {}
    flag = False
    sid=''
    for line in file:
            if re.search('^ID\s+' ,line):
                c=0
                t = line.split()[1]
                y=t.split("_")
                x=y[1]
                flag=True
                c=c+1
                sid = x
                dc[sid] = []
            elif flag and re.search("^//",line):
                flag=False
            elif flag:
                for word in line.split():
                    if word == x:
                        c=c+1
            dc[sid].append(c)
    return(dc)

def printCount(dc):
    for key,value in dc.items():
        print(f"{key} \t {value}")

def usage ():
    print('''--help|count.py filename count''')                  
                
def main(argv):
    if len(argv)<3 or sys.argv[0] == "--help":
        usage()
    else: 
        if sys.argv[2]== "count":
            dc=seqCount(argv[1])
            printCount(dc)
        else:
            print(f"Error: Valid options are: ---help|count.py filename count") 

 ## check for main script
if "__main__" == __name__:
    main(sys.argv)
