#31. Implement a program to check the elements of a list is a palindrome or not.

list= ['r','a','c','e','c','a','r']

list1 = list.copy()
list1.reverse()
if list == list1:
    print("Palindrome")
else:
    print("Not Palindrome")
