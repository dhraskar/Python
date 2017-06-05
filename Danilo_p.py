
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[10]:

T=np.arange(0,P+0.1,0.1)
print (T)


# In[26]:

To=20.0
A=70
P=24.0
Phi=-(np.pi/1)


# In[28]:

Tsup=(To+A*np.sin(2*np.pi*T/P+Phi))


# In[29]:

print (Tsup)


# In[30]:

plt.plot(T,Tsup)
plt.show()


# In[40]:

z1=0.20
z2=0.40
z3=1.00
D=0.3
Tz1=(To+A*np.sin(2*np.pi*T/P+Phi-z1/D)*np.exp(-z1/D))
Tz2=(To+A*np.sin(2*np.pi*T/P+Phi-z2/D)*np.exp(-z2/D))
Tz3=(To+A*np.sin(2*np.pi*T/P+Phi-z3/D)*np.exp(-z3/D))
plt.plot(T,Tz1,'k--',label='0.20m')
plt.plot(T,Tz2,'k:',label='0.40m')
plt.plot(T,Tz3,'k',label='1.00m')
plt.legend()
plt.xlabel("Tempo (h)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.title('Temperatura x Tempo, para diferentes profundidades')
plt.show()


# In[ ]:



