#32. Implement a program to check the total number of students. (create a sample file with RegNo, StudentName, Branch)

with open('32.csv') as csv_file:
    print("There are a total of ", len(csv_file.readlines()) - 1, " students")
