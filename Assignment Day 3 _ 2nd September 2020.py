#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Write a program to subtract two complex numbers in Python.

# In[3]:


a =2+4j
b =4+6j

c=b-a

print(c)


# # Question 2 :
# Write a program to find the fourth root of a number.

# In[6]:


a=256

print((a**(1/2))**(1/2))


# # Question 3:
# Write a program to swap two numbers in Python with the help of a temporary variable.

# In[7]:


a=10
b=5
t=a
a=b
b=t

print(a,b)


# # Question 4:
# Write a program to swap two numbers in Python without using a temporary variable.

# In[8]:


a=10
b=5
a,b=b,a

print(a,b)


# # Question 5:
# Write a program to convert Fahrenheit to kelvin and celsius both.
# 
# <h2>Formula Fahrenheit to kelvin: T(K) = (T(°F) + 459.67) × 5/9</h2>
# <h2>Formula Fahrenheit to celsius: T(°C) = (T(°F) - 32) × 5/9</h2>
# 

# In[20]:


Fahrenheit=60

kelvin = (Fahrenheit + 459.67) *(5/9)

print (kelvin,"K")

celsius = (Fahrenheit - 32) * (5/9)
print (celsius,"°C")


# # Question 6:
# Write a program to demonstrate all the available data types in Python. Hint: Use type() function.

# In[21]:


a=10
b=10.5
c=2+5j
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[ ]:




