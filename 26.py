#26. Implement a program to convert the input string to upper case (without using standard library)

str_data = 'Greshan Aranha'

result = ''
for char in str_data:
    if ord(char) >= 65:
        result += chr(ord(char) - 32)
print(result)
