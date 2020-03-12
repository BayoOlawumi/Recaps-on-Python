
# coding: utf-8

# In[ ]:


"""A positive whole number n >2 is prime if no number between 2 and √ n 
(inclusive) evenly divides n. Write a program that accepts a value of n as input 
and determines if the value is prime. If n is not prime, your program should quit as 
soon as it finds a value that evenly divides n"""
import math
try:
    n=raw_input("Enter the number you want to check. ")
    number=int(n)
    #The code below only function when the number entered is greater than 2
    if(number>2):
        counter=0
        #The sum of factor is being initiated
        for eachnum in range(2,number):
            if(number % eachnum==0):
                counter+=1
                """The loop iterates between 2 and the number before the input
                It adds to variable counter if it is a factor of number
                When there is even division."""
        if(counter==0):
            print("This number is a prime number")
           
        else:
            print("This number is not a prime number")
       
except:
    print("Please enter a real number greater than 2")


# In[ ]:


"""A formula for computing Easter in the years 1982–2048, inclusive, is as follows: 
let a =year%19, b = year%4, C =year%7, d = (19a +24)%30, e = (2b +4c +6d +5)%7. The date of Easter is March = 22 + d +e (which could be in April). Write 
a program that inputs a year, verifies that it is in the proper range and then prints 
out the date of Easter that year."""

try:
    Supplied_Input=raw_input(" Enter a year")
    year=int(Supplied_Input)
    if year>=1982 and year<=2048:
        a=year%19
        b=year%4
        c=year%7
        d=(19*a + 24)%30
        e=(2*b +4*c + 6*d +5)%7
        #print("The date of Easter is")
        print(d)
        print(e)
    else:
        print (" Year Supplied is out of range.")
except:
    print(" Wrong value submitted")


# In[19]:


"""Write a program that accepts a date in the form month/day/year and outputs 
whether or not the date is valid. For example 5/24/1962 is valid, but 9/31/2000 is 
not. (September has only 30 days.)"""

date=raw_input("Enter date in the form month/day/year")
month_with_30days=[9,4,6,11]
try:
     #Split the entered date and convert it to string
    date_S=date.split("/")
    splitted_date=([int(s) for s in date_S]) 
    validity=True
    #Condition 1, of the date is beyond 31 or the month is beyond 12
    if splitted_date[1]>31 or splitted_date[0]>12:
        print("The date is invalid")
        validity=False
    #Condition 2, if the number of days in the months with 30 days is more than 30
    if(splitted_date[1] in month_with_30days):
        if(splitted_date[1]>30):
            print("Error with the month, day number invalid")
            validity=False
    if(validity!=False):
        print("The date is valid")

except:
    print("Date is Invalid")
        

