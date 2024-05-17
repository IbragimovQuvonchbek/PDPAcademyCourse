import csv


def check_num(number: str):
    if number.isnumeric():
        return int(number)
    else:
        return 0


raw_data = []

with open('hospitals.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        raw_data.append(row[0].split(';'))

data_2012_2017 = []

for i in range(1, len(raw_data)):
    total = (check_num(raw_data[i][15]) + check_num(raw_data[i][16]) + check_num(raw_data[i][17]) +
             check_num(raw_data[i][18]) + check_num(raw_data[i][19]) + check_num(raw_data[i][20]))
    data_2012_2017.append([raw_data[i][0], total])

data_2012_2017.sort(key=lambda x: x[1], reverse=True)

first_one = data_2012_2017[0]
second_one = data_2012_2017[1]
third_one = data_2012_2017[2]

print("First:", first_one)
print("Second:", second_one)
print("Third:", third_one)
