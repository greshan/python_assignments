#24. Implement a program to read alternative characters in the file.
file = open("24.txt")
inp = file.read()
print(inp[::2])

file.close()
