#!/usr/bin/env python3

import random

d = 0

def writeResult(user,perc,task):
    out = open('results.txt', 'a')
    out.write(user + "\t" + str(perc) + "\t" + task + "\n")
    out.close()

def add(user):
    global d
    x = random.randint(10, 200)
    print("\033[33m",x, "\033[0m")
    y = random.randint(10, 200)
    print("\033[33m",y, "\033[0m")
    z = int(input("Enter your values "))
    c = x + y
    if (c == z):
        d = d + 1
        print("\033[32m Correct, The addition is ", c, "\033[0m")
    else:
        print("\033[31m Wrong answer, The addition is ", c, "\033[0m")
    writeResult(user, d * 20, 'a')


def multi(user):
    global d
    x = random.randint(2, 14)
    print("\033[33m",x, "\033[0m")
    y = random.randint(2, 14)
    print("\033[33m",y, "\033[0m")
    z = int(input("Enter your values "))
    c = x * y
    if (c == z):
        d = d + 1
        print("\033[32m Correct, The multiplication is ", c, "\033[0m")
    else:
        print("\033[31m Wrong answer, The multiplication is ", c, "\033[0m")
    writeResult(user, d * 20, 'm')

def menu(n):
    x = 0
    user = input("Enter your username: ")
    while (x < n):
        x = x + 1
        sel = input("Select: (a)dd, m(multi), (q)uit: ")
        if sel == "q":
            break
        elif sel == "a":
            add(user)
        elif sel == "m":
            multi(user)
        else:
            print("Wrong choice!")
        if x > n:
            break
    print("No of success is:", d, "/", n)


n = int(input("Enter no of iteration: (select a value greater or equal to 5)  "))
menu(n)

