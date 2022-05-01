#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st

import sys


# In[12]:


header = st.container()

dataset = st.container()

features =st.container()

modeltraining = st.container()


# In[1]:


import pandas as pd 
import altair as alt


# In[2]:


url = "https://gist.githubusercontent.com/Tulluripallavi/983092b3b60760198dc778117141ac55/raw/bbba5e8e8f1c94e297c492cd33975aa97da1f056/salesdisaster.csv"
mpg = pd.read_csv(url)


# In[ ]:


with header:
    st.title("Data visulization Project")


# In[31]:


with dataset:
    st.title("Data visulization Project 1")
    # Encoding Data using Color and Size
    chart = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_circle()# Making it as circular representation
    ).interactive()
    chart.display()# displaying the data


# In[32]:


with features:
    chart = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_bar()# Making it as circular representation
    .properties(width = 500)
    ).interactive()
    chart.display()# displaying the data


# In[17]:


with modeltraining:
    chart = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = alt.Color("location", legend=None),# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .transform_loess("Sales Agent ID", "Sales", groupby = ["State"] )
    .mark_line()# Making it as circular representation
  
    ).interactive()
    chart.display()# displaying the data


# In[ ]:




