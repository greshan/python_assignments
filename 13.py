#13. Implment a program with arithmetic functions with  case statements.

def switch_func(value, x,y):
    return {
        'a': lambda x: x+y,
        's': lambda x: x*y,
        'm': lambda x: x-y,
        'd': lambda x: x/y
    }.get(value)(x)

# take user input
'''
inp = input('input a character : ')

print('The result for inp is : ', switch_func(inp, 2))
'''
def main():

    print("Addition - 1\n")
    print("Subtraction - 2\n")
    print("Multiplication - 3\n")
    print("Division -4\n")
    num = int(input("Enter num: \n"))
    if num == 1:
        inp = input("input a for Addition : \n")
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print('The result is : ', switch_func(inp, num1, num2))
        exit()

    if num == 2:
        inp = input("input s for Subtraction : \n")
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print('The result is : ', switch_func(inp, num1, num2))
        exit()

    if num == 3:
        inp = input("input m for Multiplication : \n")
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print('The result is : ', switch_func(inp, num1, num2))
        exit()

    if num == 4:
        inp = input("input d for Division : \n")
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print('The result is : ', switch_func(inp, num1, num2))
        exit()

if __name__=="__main__":
    main()
