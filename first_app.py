# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:48:19 2021

@author: laura.woznialis
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("my first app")

st.write("here is our first attempt at using data to create table")
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    }))


"""
# my first app
here is our first attempt at using data to create table
"""

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
    })

df

###############################################

""" 
# Draw a line chart 
"""

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"])

st.line_chart(chart_data)


###############################################

""" 
# Plot a map 
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


###############################################
""" 
# Add interactivity with widgets
## Use checkboxes to show/hide data
One use case for checkboxes is to hide or show a specific chart or section in an app
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

"""
## Use a selectbox for options
You can write in the options you want, or pass through an array or data frame column.
"""

option = st.selectbox(
    'which number do you like best?',
    df['first column'])

'you selected: ', option


###############################################
""" 
# Lay out your app
For a cleaner look, you can move your widgets into a sidebar. This keeps your app central, while widgets are pinned to the left. Let’s take a look at how you can use st.sidebar in your app.
"""

option2 = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option2


"""
Most of the elements you can put into your app can also be put into a sidebar using this syntax: st.sidebar.[element_name](). Here are a few examples that show how it’s used: st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart().
"""


###############################################
""" 
# Show progress
When adding long running computations to an app, you can use st.progress() to display status in real time.
"""
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

###############################################
""" 
# 
"""



###############################################
""" 
# 
"""




###############################################
""" 
# 
"""




###############################################
""" 
# 
"""




###############################################
""" 
# 
"""




###############################################
""" 
# 
"""
