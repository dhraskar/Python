
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

get_ipython().magic('cat exemplo.dat')


# In[3]:

A=np.loadtxt("exemplo.dat")
print (A)


# In[4]:

print(A[0,0])


# In[5]:

print(A[1,2])


# In[6]:

print(A[2,1])


# In[16]:

print(A[2])


# In[17]:

print(A[1,:])


# In[18]:

print(A[:,1])


# In[21]:

print(A[1:,2:])


# In[24]:

print(A[1:3,2:4])


# In[32]:

B=np.loadtxt("exemplo.dat",skiprows=1)
print(B)


# In[34]:

print(B[0,0])


# In[35]:

print(B[1:3,2:4])


# In[33]:

C=np.loadtxt("exemplo.dat",usecols=range(1,5))
print(C)


# In[51]:

D=np.loadtxt("exemplo.dat",skiprows=1,usecols=[0,2,3])
print(D)


# In[52]:

get_ipython().magic('cat a01.txt')


# In[ ]:



