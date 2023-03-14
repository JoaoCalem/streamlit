import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from audio_recorder_streamlit import audio_recorder
import wave
import contextlib

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

AUDIO_FILE_NAME = 'myfile.wav'

audio_bytes = audio_recorder(energy_threshold=[-1.0,1.0], pause_threshold=15)
if audio_bytes:
    with open(AUDIO_FILE_NAME, mode='bw') as f:
        f.write(audio_bytes)
    with contextlib.closing(wave.open(AUDIO_FILE_NAME,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    if duration > 1:
        st.write(duration)

spell = st.secrets.section_1.secret2
st.write(spell)

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