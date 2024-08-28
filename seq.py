
#!/usr/bin/env python3

def seq(to,fro,by="1"):
    l=[]
    i=to
    while(i <= fro):
        l.append(i)
        i = i+by
    print(tuple(l))
  
seq(1,5)
