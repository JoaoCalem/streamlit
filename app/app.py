import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x = st.slider('x')  # 👈 this is a widget

st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
else:
    st.write('not selected')
    
option = st.selectbox(
    'Which number do you like best?',
     ['1','2'])

'You selected: ', option


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:

if left_column.button('Press me!'):
    test = '2'
    
    

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")