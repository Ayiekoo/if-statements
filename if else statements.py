#!/usr/bin/env python
# coding: utf-8

# In[3]:


#if <condition>:
#<block of code>
    
# example
todo_list = ['Read', 'Code', 'Watch']
if len(todo_list) < 4:
    print('To do has less than 3 items')
    
# if-else statement
# if <condition>
# <execute this block of code>
# else:
# <execute this other block of code>

# example
todo_list = ['Read', 'Code', 'Watch']
if len(todo_list) < 4:
    print('To do has less than 3 items') # when the condition is true
else:
    print('To do has more than 4 items') # when teh condition is false


# In[4]:


# example
todo_list = ['Read', 'Code', 'Watch']
if len(todo_list) < 4:
    print('To do has less than 3 items') # when the condition is true
else:
    print('To do has more than 4 items') # when teh condition is false


# In[5]:


# exercises
x = 10
if x > 6:
    print("x is greater than 6")
else:
    print("x is less than or equal to 6")


# In[6]:


x = 10
if x > 10:
    print("x is greater than 10")
elif x  == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
    
######## elif statement
########## if (condition 1>:
################<block of code>
########## elif (condition 2>:
################<block of code>
########## if (condition 3>:
################<block of code>
################ else:
################# <execute this block of code if all the other conditions are False>


# In[7]:


x = 5
y = 10
if x > 2 and y < 15:
    print("Both conditions are true")
else:
    print("At least one condition is true")


# In[9]:


# another exercise
todo_list = ['Read', 'Code', 'Watch', "Game"]
if len(todo_list) > 4:
    print('To do has more than 3 items') 
elif len(todo_list) == 4:
    print('To do has 4 items')
elif len(todo_list) !=0:
    print(' To do has less than 4 items')
else:
    print('To do has 0 items') # when teh condition is false


# In[10]:


# Nested ef-else statements
######## sometimes we make decisions based on the results of other outcomes
########### Here, we use the IF-ELIF-ELSE statements, inside the if-else statement
todo_list = ['Read', 'Code', 'Watch']

if len(todo_list) < 4:
    print('To do has less than 4 items')
    if len(todo_list) == 0: ############ == is used to determine True or False statements
        print('Todo is empty')
    elif len(todo_list) == 1:
        print('To do has 1 item')
    elif len(todo_list) == 2:
        print('To do has 2 items')
    else:
        print('To do has 3 items')
else:
    print('To do has more than 4 items')


# In[15]:


##### the use of == to determine True or false statements in python, with examples

a = 5
b = 5

print(a == b) # THIS IS A TRUE STATEMENT

c = "hello"
d = "world"

print( c == d) # THIS STATEMENT IS FALSE

e = [1, 2, 3]
f = [1, 2, 3]
print(e == f) # TRUE STATEMENT

g = {"name": "John", "age": 30}
h = {"name": "Jane", "age": 25}
print(g == h) #FALSE STATEMENT


# In[ ]:




