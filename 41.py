#41. Find the names ending with N and their count.

File = open("41.txt", 'r')
words = File.read()
File.close()
List = words.split()
#di={}
N_words = 0
for word in List:
    if word.endswith("n") == True:
        N_words +=1
print(N_words, "End the letter 'N'.")
