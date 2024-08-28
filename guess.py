#!/usr/bin/env python3
import random
import math
x = random.randint(1,25)
print(x)
n = 0
while True:
	guess = input("Guess a number:- ")
	if guess == "q":
        	break
	guess=int(guess)
	if guess == x:
         	print("\033[32m Well done!\033[0m") 
		break
		
	elif guess < x:
		print("\033[31m Guess is less\033[0m")
	elif guess > x:
		print("\033[31m Guess is more\033[0m")
	n=n+1
	print(n)
