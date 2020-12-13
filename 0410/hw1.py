#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text


# In[10]:


print(book1)


# In[11]:


print(book1[50:10000:10])

