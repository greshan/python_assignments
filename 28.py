#28. Implement a progam to convert the input string to inverse case(upper->lower, lower->upper) ( without using standard library)

str_data = 'Greshan'

result = ''
for char in str_data:
    if ord(char) >= 65 and ord(char) <= 90:
        result += chr(ord(char) - 32)
        print(result)
    elif ord(char)<=97 and ord(char) <= 123:
        result += chr(ord(char) + 32)
        print(result)
print(result)
