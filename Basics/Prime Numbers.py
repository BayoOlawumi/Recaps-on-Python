
# coding: utf-8

# In[6]:


"""A positive whole number n >2 is prime if no number between 2 and √ n 
(inclusive) evenly divides n. Write a program that accepts a value of n as input 
and determines if the value is prime. If n is not prime, your program should quit as 
soon as it finds a value that evenly divides n"""
import math
try:
    n=input("Enter the number you want to check. ")
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

