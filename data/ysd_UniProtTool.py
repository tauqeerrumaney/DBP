#!/usr/bin/env python3
# by YSD 

import sys, os, re, gzip

def usage ():
    print("Usage: filename.py datafile [getSeq getEntry getFasta] + ID | [get PubmedCount]")

class UniProtTool:
    def getEntry(self,filename,uid=''):
        '''
        Getting whole Entry for the given user id.
        '''
        if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
        else:
            file = open(filename,'rt')
        
        ID = '^ID\s+'+uid
        res = ''
        flag = False
        for line in file:
            if re.search(ID,line):
                flag = True
                res = line
            elif flag and re.search("^ID",line):
                ## If we got the previous ID and we have come onto next ID, break out of the loop.
                ## Assumption is there is every ID is unique in the file.
                break
            elif flag:
                # Until the flag is true, we keep adding the info for the ID in the result.
                res = res + line
        file.close()
        
        if res == '':
            print(f"{uid} Not Found, please try with other ID's")
            exit()
        else:
            return res
    
    def getPubmedCount(self,filename):
        '''Counting How many times each ID has been included in PubMed.'''
        if re.search('.+gz$',filename):
            file = gzip.open(filename,'rt')
        else:
            file = open(filename,'rt')
        
        id_counter = {}
        
        for line in file:
            if re.search('^ID',line):
                id = re.findall('[0-9_A-Z]{6,11}',line)
                id_counter[id[0]] = 0    
            
            if re.search('^RX',line):
                id_counter[id[0]]+=1
            
        
        return id_counter

    def printPubmedCount(self,counter):
        '''Prints the number of Pubmed counts for a given ID'''
        id_counter = dict(sorted(counter.items(), key=lambda x: len(x[0])))
        
        print("ID  \t  Value")
        
        for key,value in id_counter.items():
            if len(key)==6:
                print(key+'\t     '+str(value))
            if len(key)==7:
                print(key+'\t    '+str(value))
            if len(key)==8:
                print(key+'\t   '+str(value))
            if len(key)==9:
                print(key+'\t  '+str(value))
            if len(key)==10:
                print(key+'\t '+str(value))
            if len(key)==11:
                print(key+'\t'+str(value))
    
    def getSeq(self,filename,uid=''):
        '''
        Getting only the seq for the given ID.
        '''
        entry = self.getEntry(filename,uid)
        flag = False
        res = ''
        
        for line in entry.split("\n"):
            if re.search("^SQ\s",line):
                flag = True
                res = line+"\n"
            
            elif re.search("^//",line):
                break
            
            elif flag:
                res = res + line + "\n"
        
        return res
    
    def getFasta(self,filename,uid=''):
        '''Converting of Seq to Fasta format.'''
        seq = self.getSeq(filename,uid)
            
        line_f = seq.split('\n')[0].replace('SQ','>'+uid) #First Line
        res = line_f + '\n' 

        for i in seq.split('\n')[1:]: #Adding the amino acid seq to res, basically here the new line characters are maintained, just we remove spaces from original seq.
            res +=(re.sub("\s",'',i))
            res += '\n'
        
        return res
        
    

def main(args):
    if len(args) < 4:
        usage()
    else:
        filename = os.getcwd()+'/'+args[1]
        print(filename)
        
        if os.path.exists(filename):
            print_res = False 
            up = UniProtTool()
            if args[2] == "getEntry":
                print_res = True #025R_IIV3
                res = up.getEntry(args[1],args[3])
            
            elif args[2] == "getSeq":
                print_res = True 
                res = up.getSeq(args[1],args[3])
            
            elif args[2] == "getFasta":
                print_res = True 
                res = up.getFasta(args[1],args[3])    
                
            elif args[2] == "getPubmedCount":
                counter = up.getPubmedCount(args[1])
                up.printPubmedCount(counter)
            
            else:
                print(f"Error: Unknown option {args[2]}, valid options are 'getEntry', 'getSeq', 'getFasta', 'getPubmedCount !")
                exit()
            if print_res:
                print(res,end='')
            
        else:
            
            print(f"Error: File {args[1]} doesn't exist in the current directory")
        

 ## check for main script
if "__main__" == __name__:
    main(sys.argv)
