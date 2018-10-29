#19. Implement a program for above using getopt.

import sys
import getopt

opts,args = getopt.getopt(sys.argv[1:],"n1:n2:op:",["num1=","num2=","operand"])
print(opts)
print(args)

for key,value in opts:
	if key in ('-n1', '--num1'):
        num1 = float(value)
    elif key in ('-n2', '--num2'):
        num2 = float(value)
    elif key in ('-op', '--operand'):
        op = float(value)
if(op == '+'):
    print("sum is :"num1+num2)
elif(op == '-'):
    print("sum is :"num1-num2)
elif(op == '/'):
    print("sum is :"num1/num2)
elif(op == '*'):
    print("sum is :"num1*num2)
