#23. Implement a program to write a line from the console to a file.


inp = input("Enter text to print in file : \n")

file = open("23.txt","w")
if(file.write(inp)):
    print("written to 23.txt")

file.close()
