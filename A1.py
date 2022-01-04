

import csv
numfile = "numberfile.csv"
class assignment4:

    def readwrite(f1):
        with open(f1 , "r") as a:
            r = a.readlines ()
            for row in r:
                print(row)
    
    def sum1(f):
        with open(f, "r") as file1:
            lines = file1.readlines ()

            sum = 0

            for line in lines:
             for c in line:
                if c.isdigit() == True:
                    sum = sum + int (c)
            
            print (sum)
            file1.close()
            return sum
            

    readwrite(numfile);
    sum1(numfile)

