
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


# In[46]:

D=0.3
for z in [0.0,0.20,0.40,1.00]:
    Tz=(To+A*np.sin(2*np.pi*T/P+Phi-z/D)*np.exp(-z/D))
    plt.plot(T,Tz,label=z)
plt.legend()
plt.xlabel("Tempo (h)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.title('Temperatura x Tempo, para diferentes profundidades')
plt.show()


# In[ ]:



