#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


from matplotlib import pyplot as plt


# In[4]:


x=[1,2,3,4,5,6]
y=[12,32,56,32,5,8]
j=[12,14,2]
k=[23,89,5]
plt.plot(x,y)
plt.plot(j,k)
plt.title("test")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend(["test1","test2"])
plt.show()


# In[5]:


# ingest data


# In[6]:


sample_data= pd.read_csv('sample_data.csv')


# In[7]:


sample_data


# In[8]:


type(sample_data)


# In[9]:


# ^of data frame type defined by pandas module


# In[10]:


# retrieve second row of column b


# In[11]:


sample_data.column_b.iloc[1]


# In[12]:


#plot column a and b as x axis and y axis


# In[13]:


plt.plot(sample_data.column_a,sample_data.column_b, 'o')
plt.plot(sample_data.column_a,sample_data.column_c)

plt.title("sample data test")
plt.xlabel("x axis")
plt.ylabel("column values")
plt.legend(["sample1", "sample2"])
plt.show()


# In[14]:


# START COUNTRY DATA SET


# In[15]:


# import data


# In[16]:


data= pd.read_csv('countries.csv')


# In[28]:


data


# In[29]:


# compare china population growth


# In[39]:


china = data[data.country=='China']


# In[38]:


afghan = data[data.country == 'Afghanistan']


# In[41]:


china


# In[42]:


#plot population vs year. divide by 1000000 for samller grpah numbers


# In[48]:


plt.plot(china.year,china.population/10**6)


# In[49]:


#get top 5 populations and years


# In[52]:


china['population'].nlargest(n=5)


# In[ ]:




