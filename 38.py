#38. Create a file with patients personal records. Check for the names are properly entered. Means, no number or symbols allowed.


import csv

name = input("Patient name:\t")


if not all(c.isalpha() or c.isspace() for c in name):
    print("Name can only contain alphabtes")
    exit()

age = int(input("Patient age: "))

phone = input("Patient phone number: ")


with open('38.csv', 'a+') as csv_file:
    patient_records = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_file.seek(0)
    first_char = csv_file.read(1)
    if not first_char:
        patient_records.writerow(['Name', 'Age', 'Phone'])

    patient_records.writerow([name, age, phone])
