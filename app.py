#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import the Flask dependency
from flask import Flask


# In[6]:


#Create a New Flask App Instance, "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__)


# In[7]:


#Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'


# In[ ]:





# In[ ]:




