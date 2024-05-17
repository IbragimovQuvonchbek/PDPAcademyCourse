import csv

with open('hospitals.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0].split(';'))
