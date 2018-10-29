#17. Implement a program to get three values from CLA and print the sum of them.


import sys

args=sys.argv[1:]

sum = int(args[0]) + int(args[1]) + int(args [2])

print("Sum is :",sum)
