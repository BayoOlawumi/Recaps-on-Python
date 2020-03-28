
# coding: utf-8

# # Class
# A class is like a framework or skeleton for an object, a skeleton will have a space for the eye, the corners, the bones and all that, in short a skeleton actually defines how the body of the object will be like.

# In[4]:


#Examples
class Student:
    def __init__(self,name,matricNo,age,scores):
        self.name=name
        self.matricNo=matricNo
        self.age=age
        self.scores=scores
    
    def scoresAverage(self):
        sumVal=0
        count=0
        for score in self.scores:
            sumVal+=float(score)
            count=count+1
        averageVal=sumVal/count
        return averageVal
"This would create first object of Student class"
FirstStd=Student("Abayomi","EEE/12/0098",34,[67,56,76,56,78,90,78])
AveragedOutput=FirstStd.scoresAverage()
print("The average score of {0} with matric number {1} is {2}".format(FirstStd.name,FirstStd.matricNo,AveragedOutput))

