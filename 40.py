#40. Find the names starting with M and the count of names.


File = open("40.txt", 'r')
words = File.read()
File.close()
List = words.split()

print("Words:",len(List))

m_words = 0

for words in List:
    if words[0]=='M':
        m_words += 1
print(m_words, "start with the letter 'M'.")
