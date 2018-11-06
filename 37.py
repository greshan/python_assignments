#37. Implement a python take email id as input and check its validity using regular expressions.

import re
def isValidEmail(email):
    if len(email) > 5:
        if re.match("^.+@([]?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})()]?)$", email) != None:
            return True
    return False

inp = input("Enter valid email ID: ")
if isValidEmail(inp) == True :
    print ("This is a valid email address")
else:
    print ("This is not a valid email address")
