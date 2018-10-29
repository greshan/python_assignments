#Implement a program to reverse a string (without standard librar function)


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = "Gresha Aranha"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))
