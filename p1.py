# Assignment 2 For HeroVired Refresher Session 


# Question 2 - 

# Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 


# Sample Input - s1 -     1  4   5  6  9

# Sample Output - s2 -  1  16  25  36  81  

# code here

from tabulate import tabulate

import pandas as pd
# entries = {}

user1=int(input("Enter A Number 1 : "))

user2=int(input("Enter A Number 2 : "))

user3=int(input("Enter A Number 3 : "))

user4=int(input("Enter A Number 4 : "))

user5=int(input("Enter A Number 5 : "))

if(user1<=0 or user2<=0 or user3<=0 or user4<=0 or user5<=0):

    print("Please Enter A positive Number!")

else:
    total1 = user1*user1

    total2 = user2*user2  

    total3 = user3*user3  

    total4 = user4*user4  

    total5 = user5*user5 

    entries = {

        "SERIES" : [user1,user2,user3,user4,user5],

        "OUTPUTS" : [total1,total2,total3,total4,total5]
    }

values = pd.DataFrame(entries)

print(tabulate(values,headers = 'keys',tablefmt = 'psql')) 


