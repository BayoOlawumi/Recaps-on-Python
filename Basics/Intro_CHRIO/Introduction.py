
# coding: utf-8

# In[1]:


#Readings on variables, expression and statements
#values and types
#2,'kolawole',2.34 are values
#int, string, float are types
num=2
name='kolawole'
cgpa=2.34


# In[2]:


type(num)


# In[3]:


type(name)


# In[4]:


type(cgpa)


# In[5]:


#variables
message='I am alright'
print(message)


# In[7]:


#Statement is a line of code that can be executed by python interpreter
#examples below
a=3
print(a)


# In[10]:


#Operators and Operands
#Operators are special symbols that represents computations
a=30
b=40
c=a*b
# '*' is the operator representing multiplication
# '30' and '40' are the operands
d=b/a
# '/' represents division
e=b//a
# '//' represents floor division, giving a integer as output
print(c,d,e)


# In[11]:


#expression 
#Expression is the combination of values, operators, operands.
#In a script, an expression by itself does not necessarily do anything
#***********Example *****************#
#x+1
#x=5


# In[12]:


#Order of Operations
#PEMDAS
#Parenthesis-Exponential-Multiplication-Division-Addition-Subtraction
a=2*5+(3/3)+2**3
#2*5+1+2**3
#2*5+1+8
#10+1+8
#Output=19
a


# In[13]:


#Mudulos Operator
a=5
b=3
c=5 % 3
print(c)
#This gives the remainder


# In[15]:


#String Operation
lastname='Olawumi'
firstname='Abayomi'
fullname=lastname+firstname
print(fullname)


# In[ ]:


input = input()

