#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {'X': ['-117.084279', '-118.332261', '-118.30621'],
        'Y': ['32.6409', '34.003849', '34.061693'], 
        'Vendor': ['Quasar', 'Excelsior', 'Excelsior'],
        'Address': ['Chula Vista, CA', '4371 Crenshaw Blvd, Los Angeles, CA, 90008', '3680 Wilshire Blvd, Los Angeles, CA, 90010'],
        'Annual_Sales': ['534233', '105585', '105585'],
        'Zip': ['0', '90008', '90010'],
        'Region': ['South', 'South', 'South']}


# In[3]:


df = pd.DataFrame(data=['X',  'Y',  'Vendor', 'Address', 'Annual_Sales', 'Zip', 'Region'])


# In[4]:


df = pd.DataFrame(data=data)


# In[5]:


df


# In[6]:


ax = df.plot.bar(x='Annual_Sales', y='Zip', rot=0)


# In[7]:


ax = df.plot.bar(x='X', y='Y', rot=0)


# In[8]:


ax = df.plot.bar(rot=0)


# In[9]:


ax = df.plot.bar(x='Zip', y='Annual_Sales', rot=0)


# In[ ]:




