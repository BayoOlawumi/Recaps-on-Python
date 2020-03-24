
# coding: utf-8

# In[1]:


#Multline Statements
#You use the backlash to continue statement
a=2+3+4+4
print(a)


# In[2]:


#Multiple Statements
#You can assign statement
a,b,c=45,34,23
print(a)
print(b)
print(c)
d=4;e=5
print(d)
print(e)


# In[5]:


#python input and output
name="Olawumi"
age=29
print("Mr {0} is {1} years old".format(name,age))
print("Mr {1} is {0} years old".format(name,age))


# In[4]:


#python input and output
print("Mr {name} is {age} years old".format(name='Olawumi',age=25))


# In[28]:


#Operators
#Basic
x,y=10,20
div=x/y
print(div)
flr=x//y
print(flr)
#This operator gets the floor division of x and y, return the nearest whole number
#There are many more mathematical/basic operators
#******************************************************#



# In[29]:


#Logical
a=True
b=False
c=a and b
print(c)
d=a or b
print(d)



# In[24]:


#Membership Operator
#Checking if an element is a member of a set
a=[2,3,5,6,7,7]
b=2 in a
print(b)
d={name:"Kolapo", age:2}
e=age in d
print(e)


# In[30]:



f,g=3,4
#Bitwise 
#Binary Representation of 3=011 and 4=100
h=f&g
print(h)
i=f|g
print(i)




# In[31]:


#Assignment Operators
a=2
b=3
c=4
d=5

# a=a+1 is the same as a+=1
a=a+1
b+=1
#It adds 1 to the value of b and storesit inside b
print(a)
print(b)

c**=2
print(c)


# In[25]:


#identity Operator
#Checking if an element equates another
a=4
b=5
print(a is b)


# In[26]:


d=3
e=3
print(d is e)


# In[27]:


#This identity operator is invalid for complex identifier such as List
r=[1,2,3,4,5]
t=[1,2,3,4,5]
print(r is t)


# In[32]:


#To get your current working directory
pwd

