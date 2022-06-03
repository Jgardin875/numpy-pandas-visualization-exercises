#!/usr/bin/env python
# coding: utf-8

#!!!!!!! Grader: 

## I have uploaded this as numpy_exercises.ipynb and more_numpy_practice.ipynb to the same repo if you prefer jupyter notebook. 
## This is the combination of numpy_exercises.ipynb and more_numpy_practice.ipynb and converted to .py format

# In[1]:


import numpy as np


# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[3]:


np.count_nonzero(a < 0)


# In[4]:


np.count_nonzero(a > 0)


# In[5]:


np.count_nonzero((a > 0) & (a % 2 == 0))


# In[6]:


b = a + 3
np.count_nonzero(b > 0)


# In[7]:


c = a ** 2
print(a.mean())
a.std()


# In[8]:


cent_funct = lambda x: x - x.mean()
centered_a = cent_funct(a)
print(centered_a)
print(centered_a.mean())


# In[9]:


z_score = (a - a.mean())/a.std()
print(z_score)


# In[ ]:


#MORE NUMPY EXERCISES



#!/usr/bin/env python
# coding: utf-8

# ## Setup 1

# In[1]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #np.array(a) till then it is list


# In[2]:


sum_of_a = sum(a) #why not a.sum()? # a.sum() would work if it was an array
print(sum_of_a)


# In[3]:


min_of_a = min(a)
print(min_of_a)


# In[4]:


max_of_a = max(a) 
print(max_of_a)


# In[5]:


mean_of_a = sum(a)/len(a) #built in python method


# In[6]:


import statistics #an import method


# In[7]:


mean_of_a = statistics.mean(a)


# In[8]:


def product_of_a(alist):
    q = 1
    for x in alist:
        q *=x
    return q
product_of_a(a)


# In[9]:


# !! not gonna work: squares_of_a = a ** 2 #need for loop or comprehension for list (append)

# sqr = lambda x: x * x
# sqr(a)
# TypeError: can't multiply sequence by non-int of type 'list'

sqr_list = [x**2 for x in a]
sqr_list


# In[10]:


import numpy as np #for comparison


# In[11]:


np.power(a, 2)


# In[12]:


odds_in_a = [x for x in a if x % 2 != 0]
odds_in_a


# In[13]:


evens_in_a = [x for x in a if x % 2 == 0] 
# note that a % 2 == 0 wont work cuz its a list, 
# so you need a loop to hit each element in the list (but numpy could do it, it's designed for vector operations)
# TypeError: unsupported operand type(s) for %: 'list' and 'int'


# ## Setup 2

# In[14]:


c = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[15]:


b = np.array(c)
print(b)


# In[16]:


b.sum()


# In[17]:


b.min()


# In[18]:


b.max()


# In[19]:


b.mean()


# In[20]:


b**2


# In[27]:


b % 2 != 0


# In[28]:


b[b% 2 !=0]


# In[30]:


b % 2 == 0


# In[31]:


b[b% 2 ==0]


# In[32]:


b.shape


# In[33]:


b.transpose


# In[34]:


np.transpose(b)


# In[37]:


np.reshape(b, (1,6))


# In[38]:


np.reshape(b, (6,1))


# ## Setup 3

# In[40]:


t =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[41]:


c = np.array(t)


# In[42]:


print(c)


# In[43]:


np.std(c)


# In[47]:


np.var(c)


# In[46]:


print(c.shape)


# In[45]:


print(np.transpose(c))


# In[49]:


np.dot(c,c)


# In[54]:


np.sum(c* np.transpose(c))


# In[55]:


c*np.transpose(c) #!!!!!!!!!!!!!# wrong answer


# ## Setup 4

# In[56]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# In[57]:


d


# In[58]:


np.sin(d)


# In[59]:


np.cos(d)


# In[60]:


np.tan(d)


# In[61]:


d[d<0]


# In[62]:


d[d>0]


# In[64]:


np.unique(d)


# In[65]:


d.shape


# In[68]:


np.shape(np.transpose(d))


# In[70]:


np.reshape(d, (9, 2))


# In[ ]:




