#!/usr/bin/env python
# coding: utf-8

# # Assignment 
# 

# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.

# In[ ]:


l=[x for x in range(2000,3201) if (x%7)==0 and (x%5)!=0]
for i in l:
    print(i,end=",")


# printed in the the reverse order with a space between first name and last name

# In[ ]:


f_name=input()
l_name=input()
print(l_name," ",f_name)


# In[ ]:


Write a Python program to find the volume of a sphere with diameter 12 cm.


# In[ ]:


import math
d=12
r=d/2
v=4/3*math.pi*pow(r,3)
print(v)

