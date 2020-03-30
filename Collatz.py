# Programmer: Matthew Landes
# Date:		  March 11, 2020

import time

def collatz(number):
  if number % 2 == 0:
    n = number // 2
    print(n)
  else:
    n = 3 * number + 1
    print(n)
  return n

print('Please enter any integer')
n = input()
number = int(n)

while number > 1:
  number = collatz(number) 
time.sleep(20)