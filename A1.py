

import csv
numfile = "numberfile.csv"

# class is example of encapsulation
class assignment4:
    
    def readwrite(f1):
        with open(f1 , "r") as a:
            r = a.readlines ()
            for row in r:
                print(row)
    
    def sum1(self,f):
        with open(f, "r") as file1:
            lines = file1.readlines ()

            sum = 0

            for line in lines:
             for c in line:
                if c.isdigit() == True:
                    sum = sum + int (c)
            
            print (sum)
            file1.close()
            
            

    readwrite(numfile);

#inheritance
class assgn4(assignment4):
    #polymorphism
    def sum1(self):
        print('sum')

#object created
o1 = assignment4()
o2 = assgn4()

o1.sum1(numfile)
o2.sum1()




