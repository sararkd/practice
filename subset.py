
import sys
number = 0

def printSubsets(s, l):
    global number
    if len(s) == 0:
        number += 1 
        print number, ":\t", l
    else: 
        printSubsets(s[:-1], l)
        printSubsets(s[:-1], l + [s[-1]])

s = [1,2, 3, 4, 5]
printSubsets(s, [])