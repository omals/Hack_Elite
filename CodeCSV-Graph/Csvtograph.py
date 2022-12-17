import streamlit as st
import pandas as pd
import numpy as np

st.title('CSV DATA to Graph ')

DATA_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATA_COLUMN] = pd.to_datetime(data[DATA_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Done! (using st.cache)')

if st.checkbox('show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Uber csv data :Number of pick up to hours')

hist_values = np.histogram(
    data[DATA_COLUMN].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(hist_values)

st.header('Map of all pickups')
st.map(data)

hour_of_filter = 17
filtered_data = data[data[DATA_COLUMN].dt.hour == hour_of_filter]
st.subheader(f'Map of all pickups at {hour_of_filter}:00')
st.map(filtered_data)


chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)

hour_of_filter = st.slider('hour',0,23,17)