#!/usr/bin/env python3

import random

d=0

def add():
    global d
    x=random.randint(10,200)
    print(x)
    y=random.randint(10,200)
    print(y)
    z=int(input("Enter your values "))
    c=x+y
    if(c==z):
        d=d+1
        print("\033[32m The addition is ", c,"\033[0m")
    else:
	print("\033[31m The addition is ", c,"\033[0m")
    

def multi():
    global d
    x = random.randint(2, 14)
    print(x)
    y = random.randint(2, 14)
    print(y)
    z=int(input("Enter your values "))
    c = x * y
    if(c==z):
        d=d+1
    print("\033[32m The Multiplication  is ", c, "\033[0m")

def menu(n):
    x=0
    while (x<n):
        x = x + 1
        sel = input("Select: (a)dd, m(multi), (q)uit: ")
        if sel == "q":
            break
        elif sel == "a":
            add()
        elif sel == "m":
            multi()
        else:
            print("Wrong choice!")
        if x > n:
            break
    print("No of sucess is:",d,"/",n)

n=int(input("Enter no of iteration: (select a value greater or equal to 5  "))
menu(n)   
