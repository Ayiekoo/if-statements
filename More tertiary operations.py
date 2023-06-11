#!/usr/bin/env python
# coding: utf-8

# In[1]:


## let's see what happens in this code
a, b = 10, 20 ## the tuple of the two elements

print( (b, a) [a < b])

"""
(b, a) creates a tuple with two elements, b and a.

a < b is a comparison that results in a boolean value (True or False). Since a is 10 and b is 20, a < b is True.

In Python, True is also considered to be 1, and False is considered to be 0. 
So you can use True and False as indices to access elements in a list or tuple.

Therefore, (b, a) [a < b] means "create a tuple with b and a, 
and then return the first element if a < b is False (i.e., if a is not less than b), 
or the second element if a < b is True (i.e., if a is less than b)."

Given that a is 10 and b is 20, a < b is True, which as an index corresponds to 1. 
So, (b, a) [a < b] returns the second element of the tuple, which is a, or 10. Hence, the print statement outputs 10.
"""


# In[2]:


x = 76
if x > 1:
    print("May day")
else:
    print("Aye")


# In[3]:


grade = 85

if grade >= 90: ### FALSE
    print("A")
elif grade >= 80: ### TRUE
    print("B")
elif grade >= 70: ### TRUE
    print("C")
elif grade >= 60: #### TRUE
    print("D")
else:
    print("F")


# In[ ]:




