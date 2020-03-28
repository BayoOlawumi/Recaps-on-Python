
# coding: utf-8

# ## Method

# In[1]:


#we will be discussing about class and methods 
#Methods are section or set of programming statement dedicated to carry out a function
#Example 1
def Multiplier(age):
    print(age*2)
#The name of the method here is #Multiplier with a single parameter
#age is called parameter, the represents value that are passed in.
Multiplier(20)


# In[3]:


#A method cannot only excute some statements but can also return value
#Example 2
#In the method below, nums is the parameter with the datatype "List"
def FindMean(nums):
    total=0
    #iterates over the list supplied
    for a in nums:
        total+=a
    meanVal=total/len(nums)
    return meanVal
nums=[2,3,4,5,6,7,8,4,2,5,6]
#The evaluated mean value get returned to the variable meanReceived
meanReceived=FindMean(nums)
print("The mean of {0} is {1}".format(nums,meanReceived))
#If you can remeber the print format I introduced in the class, I used that here.


# In[4]:


#A little digression,The above problem can actually be solve using a library actually
import numpy as np
nums=[2,3,4,5,6,7,8,4,2,5,6]
meanEvaluated=np.mean(nums)
print("The mean of {0} is {1}".format(nums,meanEvaluated))
#I actually used the approach in the former kernel to explain that a method can return a value
#you can pass any value of any datatype as parameter to the method
#As you can see here, a list was passed to the method


# ## Assignment
# 
# Write a method that collects the scores of a students as a dictionary, with the coursecodes as keys and the score as values, this method should calculate the GPA of the student forthat semester asssuming all courses are 3 units, the number courses may vary. The GPA for the semester should be returned.
# -------Ensure you put enough comments for clarity.--------
