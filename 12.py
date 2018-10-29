#12. Implement a program with lamda functions, for finding the area of circle, triangle, square.

'''
def circle(r):
    return lambda r : 3.14*r*r

def triangle(h,b):
    return lambda h, b : (h*b)/2

def square(s):
    return lambda s : s*s
'''

circle = lambda r : 3.14*r*r
triangle = lambda h, b : (h*b)/2
square = lambda s : s*s;
def main():

    print("Area of Circle - 1\n")
    print("Area of Triangle - 2\n")
    print("Area of Square - 3\n")
    num = int(input("Enter num: \n"))
    if num == 1:
        r = float(input("Enter radius value:\t"))
        a = circle(r)
        print("\nArea is : ", a)
        exit()

    if num == 2:
        h = float(input("Enter Height values:\t"))
        b = float(input("Enter Base values:\t"))
        a1 = triangle(h,b)
        print("\nArea is : " ,a1)
        exit()

    if num == 3:
        s = float(input("Enter side value:\t"))
        a2 = square(s)
        print("\nArea is : " ,a2)
        exit()

if __name__=="__main__":
    main()
