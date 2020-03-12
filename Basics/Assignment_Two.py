
# coding: utf-8

# In[22]:


#A program to check if a positive integer value is a power of 2
val=input("Enter a postive integer ")
import math
try:
    num=int(val)
    evaluated=math.log(num)/math.log(2)
    trimmed=round(evaluated)
    if(math.pow(2,trimmed) == num):
        print("The integer entered is a power of 2")
    else:
        print("The integer entered is not a power of 2")
except:
    print("Invalid input supplied")


# In[33]:


#Write a program that accepts six(6) numbers and sorts them in descending order
list_num=[]
try:
    for a in range(4):
        val=input("Enter value ")
        list_num.append(val)
    list_num=list(map(int,list_num))
    list_num.sort()
    print(list_num)
except:
    print("Invalid input")


# In[2]:


#Write a program that sum all numeric values in a sentence
#Sample sentence: 3 eggs in 2 baskets, the output will be 5
try:
    sentence=input("Enter a sentence ")
    sent_split=sentence.split()
    sum_all=0
    for a in sent_split:
        checkint=len(a)
        countint=0
        for b in a:
            if(b.isdigit()):
                countint+=1  
        if(checkint==countint):
            sum_all=sum_all+int(a)
    print(" The sum of numeric values in this sentence is: ",sum_all) 
    print(sum_all)
except:
    print("Invalid Input")


# In[6]:


#write a program to calculate the sum of the modulus of four integer numbers
try:
    sum_of_all=0
    for a in range(4):
        val=input("Enter value ")
        sum_of_all=sum_of_all+int(val)%2
    print("The sum of the modulo 2 of the four numbers are :", sum_of_all)
except:
    print("Invalid supply")

