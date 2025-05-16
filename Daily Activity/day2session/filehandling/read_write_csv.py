""" CSV Handling in Python"""

# reading and writing list data to csv file

import csv

data = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 21, "A"]
]

with open ('stud_data.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

#Read the CSV File

with open("stud_data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)