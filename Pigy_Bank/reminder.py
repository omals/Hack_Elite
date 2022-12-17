import streamlit as st
import time
import pandas as pd
def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
#write=st.write("Time Up!")
#max_sa
#if(max_save==)
def main():
    st.title("PIGGY BANK <3")
    time_days = st.number_input('Enter number of min to save amount ', min_value=1, max_value=31)
    time_in_seconds = time_days * 60
    save_money=st.number_input('Enter amount to achieve a goal:',min_value=1*10, max_value=100)
    days=st.number_input('Enter amount to piggy bank:',min_value=10,max_value=100)
    #time_in_days=time_in_seconds/86400
    df = pd.DataFrame({
    'money': [10,20,50],
    #'month': ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'],

    })
    sum_save=0
    #return save_money
    i=0
    j=0
    for i in range(1):
        #to_select=st.selectbox('Day to be selected:',days)
        j=j+1
        to_save = st.selectbox('Amount to be saved today:',
        df['money'])
        sum_save=sum_save+save_money



    #sum_to_save=

    if st.button("START"):
        count_down(int(time_in_seconds))
        if (count_down(time_in_seconds)==0|save_money==to_save):
            write=st.write("You have saved money successfully :)\n")
        elif(count_down(time_in_seconds)==0|save_money!=to_save):
            write=st.write("You have not reached your goal :(")

if __name__ == '__main__':
    main()





