# Programmer: Matthew Landes
# Date:		  March 14, 2020

import time
import sys

user_list = sys.argv[1].split(',')
print(user_list)


def list_to_str(somelist):
    holder = ''
    near_end = len(somelist) - 2
    the_end = len(somelist) - 1
    for i in range(0,len(somelist)):
        if i == near_end:
            holder = holder + somelist[i] + ', and '
        elif i == the_end:
            holder = holder + somelist[i]
        else:
            holder = holder + somelist[i] + ', '
    return holder

print(list_to_str(user_list))

time.sleep(5)

