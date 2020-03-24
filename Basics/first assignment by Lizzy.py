#1.PROGRAM TO PRINT IDENTITY
name=raw_input('enter your name:')
print ('that is it')
matric=raw_input('enter your matric number here')
print ('identity noted')

#2. PROGRAM TO PERFORM ARITHMETIC OPERATIONS
a=5
b=7
c=6
d=8
average=(a*b-c+d)/7
print ('the average is' , average)
#to make the program more detailed
a=input('enter the first number')
b=input('enter the second number')
c=input('enter the third number')
d=input('enter the forth number')
average=(a*b-c+d)/7
print ('the average is' , average)

#3.PROGRAM TO STORE STUDENTS SCORES AND MATRIC NUMBER
studScores=[49,56,65,78,32,80,77,66,50]
studScores[4]=78
studScores[8]=77
for singlescore in studScores:
    print singlescore
#matric numbers and names of 20 students using python dictionary
deptDict={'mcb/17/4650':89,'mcb/17/4651':78,'mcb/17/4652':66,'mcb/17/4653':80,'mcb/17/4654':56,'mcb/17/4655':67,'mcb/17/4656':54,'mcb/17/4657':45,'mcb/17/4658':77,'mcb/17/4659':93,'mcb/17/4660':39,'mcb/17/4661':72,'mcb/17/4662':81,'mcb/17/4663':55,'mcb/17/4664':63,'mcb/17/4665':79,'mcb/17/4666':89,'mcb/17/4667':93,'mcb/17/4668':46,'mcb/17/4669':23,'mcb/17/4670':50}
for key in deptDict:
    print key,deptDict[key]
    
    
