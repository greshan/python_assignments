#39. Find the average number of students from records.
import csv

with open('39.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    students = list()
    branches = list()
    for row in csv_reader:
        students.append(row['RegNo'])
        branches.append(row['Branch'])

    avg = len(students) / len(branches)

print("Average number of students are: ",avg)
