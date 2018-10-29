#Create a list with 5 branches in SOIS. Try to do the following operations a) append b) insert c) sort d) reverse sort

lis = ['MSD', 'VIR', 'EWT', 'BDA', 'ESD']


lis.append('SOIS')

print("List elements after APPENDING are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

print("\r"


lis.insert(2, 'SOIS')


print("List elements after inserting 4 are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

print("\r"

lis.sort()


print ("List elements after sorting are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

print("\r")


lis.reverse()


print ("List elements after reversing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
