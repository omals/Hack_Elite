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
    save_money=st.number_input('Enter amount to achieve a goal:',min_value=0,max_value=100)
    no_days=st.number_input('Enter amount of days to enter money:',min_value=1,max_value=9)
    #time_in_days=time_in_seconds/86400
    df = pd.DataFrame({
    'money': [0,10,20,50],
    #'days':[1,2,3,4,5,6,7,8,9]
    })
    i=0

    sum_save=0
    if(i!=no_days):
        day=st.number_input('Enter the day of the month you save:',min_value=1,max_value=31)
        to_save = st.selectbox('Amount to be saved today:',
    df['money'])
        sum_save=sum_save+to_save
        i=i+1
        write1=st.write("You have saved:",sum_save," in this month now ",no_days," left!!")
    if st.button("START"):
       count_down(int(time_in_seconds))
    if(sum_save==save_money):

           write=st.write("You have saved money successfully :)\n")
    elif(sum_save!=save_money):
           write=st.write("You have not reached your goal :(")



    #return save_money





    #sum_to_save=



if __name__ == '__main__':
    main()





