#!/usr/bin/env python
# coding: utf-8

# Check whether a given number is odd or even

# In[2]:


a=int(input("Enter the number"))
if(a%2==0):
    print("Even")
else:
    print("Odd")


# Check whether a given number is vowel or consonant

# In[3]:


x=input("Enter a character to check whether a given number is vowel or consonant")
if(x == 'a' or x == 'e' or x == 'i' or
        x == 'o' or x == 'u' or x == 'A' or
        x == 'E' or x == 'I' or x == 'O' or
        x == 'U'):
    print("Vowel")
else:
    print("consonant")


# check whether a person is eligible to vote or not

# In[4]:


a= int(input("Enter the age to check whether you are eligible for vot or not"))
if(a>18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


# check whether a given number is positive/negative/Zero

# In[6]:


a=int(input("Enter the numver to check positive/negative/Zero "))
if(a>=1):
    print("Positive")
elif(a==0):
    print("Given number is Zero")
elif(a<1):
    print("Given number is negative")


# check whether given number is leap year or not

# In[9]:


a=int(input("Enter the number to check whether given number is leap year or not"))
if(a%4==0):
    print("Given number is Leap year")
else:
    print("Given number is not Leap year ")


# Write a Python program to check a triangle is equilateral, isosceles or scalene.

# In[11]:


print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")


# write a program to check whether after selling a product its profit or loss

# In[19]:


cp=float(input("Ente the cost price"))
sp=float(input("Enter the Selling price"))
if(cp>sp):
    print("It is loss",cp-sp)
elif(sp>cp):
    print( "It is profit",sp-cp)
    


# In[ ]:




