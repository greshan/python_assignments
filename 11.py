#Implement a program with functions, for finding the area of circle, triangle, square.


def main():
    print("Area of Circle - 1\n")
    print("Area of Triangle - 2\n")
    print("Area of Square - 3\n")
    num = int(input("Enter num: \n"))
    if num == 1:
        r = float(input("Enter radius value:\t"))
        a = 3.14*r*r
        print("\nArea is : ", a)
        exit()

    if num == 2:
        h = float(input("Enter Height values:\t"))
        b = float(input("Enter Base values:\t"))
        a1 = (h*b)/2
        print("\nArea is : " ,a1)
        exit()

    if num == 1:
        s = float(input("Enter side value:\t"))
        a2 = s*s
        print("\nArea is : " ,a2)
        exit()

if __name__=="__main__":
    main()
