#25. Implement a function to count the number of vowels present in the file.


file  = open("25.txt")
str = file.read()


count = 0
vowel = set("aeiouAEIOU")

for alphabet in str:
    if alphabet in vowel:
        count = count + 1
print("No. of vowels :", count)

file.close()
