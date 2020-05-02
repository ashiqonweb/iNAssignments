#!/usr/bin/env python
# coding: utf-8

# # Question1
# 
# 1. Create the below pattern using nested for loop in Python
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 

# In[18]:


n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("")
    


# # Question 2
# Write a Python program to reverse a word after accepting the input from the user.

# In[20]:


inpstr=input("Enter your string :")
print(inpstr[::-1])

