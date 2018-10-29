#20. Implement a program for above using Argparse.


import sys
import argparse

parser = argparse.ArgumentParser(description='Argparse')
parser.add_argument('-n1', '--num1',type=float, required=True)
parser.add_argument('-n2', '--num2', type=float,required=True)
parser.add_argument('--op', required=True)

args = parser.parse_args()

if(args.op == '+'):
    sum = args.num1 + args.num2
    print(sum)
elif(args.op == '-'):
    diff = args.num1 - args.num2
    print(diff)
elif(args.op == '*'):
    mul = args.num1 * args.num2
    print(mul)
elif(args.op == '/'):
    div = args.num1 / args.num2
    print(div)
