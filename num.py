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


# In[14]:


with dataset:
    st.title("Data visulization Project 1")
    # Encoding Data using Color and Size
    chart1 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_circle()# Making it as circular representation
    ).interactive()
    chart1.display()# displaying the data


# In[15]:


with dataset:
    chart2 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_bar()# Making it as circular representation
    .properties(width = 500)
    ).interactive()
    chart2.display()# displaying the data


# In[17]:


with dataset:
    chart3 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = alt.Color("location", legend=None),# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .transform_loess("Sales Agent ID", "Sales", groupby = ["State"] )
    .mark_line()# Making it as circular representation
  
    ).interactive()
    chart3.display()# displaying the data


# In[18]:


with dataset:
    chart4 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Sales',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Sales', 'State']
    )
    .mark_rect()# Making  representation
    ).interactive()
    chart4.display()# displaying the data


# In[19]:


with dataset:
    chart5 = (alt.Chart(mpg)# including the csv file
    .encode(
    x='Sales Agent ID', # adding the X value
    y='Quantity',# adding the Y value
    color = "State",# adding the color value
    tooltip=['Sales Agent ID', 'Quantity', 'State']
    )
    .mark_boxplot()# Making it as boxplot representation
    ).interactive()
    chart5.display()# displaying the data


# In[30]:


with dataset:
    selection= alt.selection_multi(fields=['State'],bind='legend')
    chart6 = (alt.Chart(mpg)
    .encode( 
    y='Sales',
    color = "State",
    opacity=alt.condition(selection, alt.value(1),alt.value(0)),
    ).add_selection(selection)
    .mark_point()
    ) 
chart6.encode(x='Sales Agent ID')|chart6.encode(x='Zip Code')


# In[ ]:




