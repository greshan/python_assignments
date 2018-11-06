#42. Read the regno and name in the file, create a dictinary of these data.

import csv

with open('42.csv') as f:
    reader = csv.DictReader(f)
    results = {d.pop('RegNo'): dict(d) for d in csv.DictReader(f)}

print(results)
