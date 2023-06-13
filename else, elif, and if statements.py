#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## if, elif, else

"""
Conditional program execution:
program starts with "If" branch, tries the "elif" branches,
and finishes with "else" branch (until one branch evaluates to True)
"""


# In[1]:


x = int(input("your value: "))
if x > 3:
    print("Big")
elif x == 3:
    print("Medium")
else:
    print("Small")


# In[2]:


x = int(input("your value: "))
if x > 3:
    print("Big")
elif x == 3:
    print("Medium")
else:
    print("Small")
    


# In[3]:


x = int(input("your value: "))
if x > 3:
    print("Big")
elif x == 3:
    print("Medium")
else:
    print("Small")


# In[4]:


### grading system
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Your grade is {grade}.')


# In[5]:


### traffic lights
traffic_light = 'Yellow'

if traffic_light == 'Red':
    print("Stop")
elif traffic_light == 'Yellow':
    print("Prepare to stop")
else:
    print("Go")


# In[6]:


### age group

age = 15

if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# In[7]:


age = 75

if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# In[8]:


age = 25

if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# In[ ]:




