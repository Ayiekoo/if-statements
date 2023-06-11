#!/usr/bin/env python
# coding: utf-8

# In[2]:


### value_if_true if condition else value_if_false

## example
# is_nice = True
# state = "nice" is is_nice else "not nice"

nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)


# In[3]:


nice = False
personality = ("mean", "nice")[nice]
print("The cat is ", personality)


# In[4]:


### let's do another exercise
arrogant = False
behavior = ("humble", "arrogant")[arrogant]
print("My son is ", behavior)


# In[5]:


### let's do another exercise
arrogant = True
behavior = ("humble", "arrogant")[arrogant]
print("My son is ", behavior)


# In[6]:


### another example

x = 35
y = 25

print("Yellow") if x > y else print("Tuesday")


# In[10]:


a = 35
b = 33

print("Hurray") if a > b else print("May Day")


# In[ ]:




