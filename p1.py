# Assignment 2 For HeroVired Refresher Session 


# Question 2 - 

# Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 


# Sample Input - s1 -     1  4   5  6  9

# Sample Output - s2 -  1  16  25  36  81  

# code here

from tabulate import tabulate

import pandas as pd
# entries = {}

n1=int(input("Enter A Number 1 : "))

n2=int(input("Enter A Number 2 : "))

n3=int(input("Enter A Number 3 : "))

n4=int(input("Enter A Number 4 : "))

n5=int(input("Enter A Number 5 : "))

if(n1<=0 or n2<=0 or n3<=0 or n4<=0 or n5<=0):

    print("Please Enter A positive Number!")

else:
    total1 = n1*n1

    total2 = n2*n2  

    total3 = n3*n3  

    total4 = n4*n4  

    total5 = n5*n5 

    entries = {

        "SERIES" : [n1,n2,n3,n4,n5],

        "OUTPUTS" : [total1,total2,total3,total4,total5]
    }

values = pd.DataFrame(entries)

print(tabulate(values,headers = 'keys',tablefmt = 'psql')) 


