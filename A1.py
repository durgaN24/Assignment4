

import csv
with open('numberfile.csv', 'r') as a:
    r = csv.reader(a)
    for row in r:
        print(row)


given_file = open('numberfile.csv', 'r')

lines = given_file.readlines ()

sum = 0

for line in lines:
    for c in line:
        if c.isdigit() == True:
            sum = sum + int (c)

print (sum)

given_file.close()