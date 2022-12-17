import streamlit as st
import time
prev_total_ex=15,000
this_total_ex=10,000
if(prev_total_ex<this_total_ex):
    st.warning('This is a warning', icon="⚠️")
else:
    st.balloons()
    my_bar = st.progress(0)
    for percent_complete in range(100):
      time.sleep(0.1)
      my_bar.progress(percent_complete + 1)
    st.success('You have achieved your goal!!', icon="✅")
