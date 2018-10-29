#18. Implement a program using CLA for simple arithmetic calculator exmaple: operand operator operand ie. 10 + 10 / 30 * 20

import sys

args = sys.argv[1:]
print("operand operator operand\n")
str(args[2])
if args[2] == '+':
    sum = float(args[1]) + float(args[3])
    print("Sum is : ",sum)
    exit()

if args[2] == '-':
    sub = args[1] - args[3]
    print("Sum is : ",sub)
    exit()

if args[2] == '*':
    mul = args[1] * args[3]
    print("Sum is : ",mul)
    exit()

if args[2] == '/':
    div = args[1] / args[3]
    print("Sum is : ",div)
    exit()
