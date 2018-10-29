#Implement a  program to check the elements in the list has word "SOIS"


list_of_elements = ['VIR', 'BDE', 'VLSI', 'ME', 'SOIS', 'EWT']

x = input("Enter String to search: ")

found = False

for i in range(len(list_of_elements)):
 if(list_of_elements[i] == x):
  found = True
  print("%s found at %dth position"%(x,i))
  break

if(found == False):
 print("%s is not in list"%x)
