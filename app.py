import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
from datetime import datetime
import pickle
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.ensemble import RandomForestClassifier
# Days_fly 	destination 	deptime 	arrtime 	duration 	stops 	Day_Name 	d_month 	s_month 	diff_month 	search_day
def main():
    st.title('I N D I G O')

    dep_date = st.date_input('date of travel',value= None)
    dest = st.selectbox('Select Destination',['BOM','HYD','NAG','PNQ'])
    destn = 1
    if dest == 'BOM':
        destn = 1
    elif dest == 'HYD':
        destn = 2
    elif dest == 'PNQ':
        destn = 4
    else :
        destn = 3
    #dep_time = st.selectbox("Departure Time",['12 Mid-Night to 6 A.M.','6 A.M to 12 Noon','12 Noon to 6 P.M.','6 P.M. to 12 Mid-Night'])
#
    #if dep_time == '12 Mid-Night to 6 A.M':
    #    dep_time = 1
    #elif dep_time == '6 A.M to 12 Noon':
    #    dep_time = 2
    #elif dep_time == '6 P.M. to 12 Mid-Night':
    #    dep_time = 4
    #else :
    #    dep_time = 3
#
    #arr_time = st.selectbox("Arrival Time",['12 Mid-Night to 6 A.M.','6 A.M to 12 Noon','12 Noon to 6 P.M.','6 P.M. to 12 Mid-Night'])
    #if arr_time == '12 Mid-Night to 6 A.M':
    #    arr_time =1 
    #elif arr_time == '6 A.M to 12 Noon':
    #    arr_time = 2
    #elif arr_time == '6 P.M. to 12 Mid-Night':
    #    arr_time = 4
    #else :
    #    arr_time = 3
    stops = st.selectbox('No. of Stops',[0,1,2])
    days2fly = (dep_date - datetime.today().date()).days

    #duration = 140
    #if stops == 1:
    #    duration = 280
    #elif stops == 2:
    #    duration = 400

    day_name = dep_date.weekday()
    dep_month = dep_date.month
    s_month = datetime.today().date().month
    d_month = dep_month - s_month
    search_day = datetime.today().date().day

    features = [days2fly,destn,stops,day_name,dep_month,s_month,d_month,search_day]
    features2 = [np.array(features)]

    #st.write(features)

    #@st.cache
    #def load_model():
    #    filename = "knn_model.pkl"
    #    loaded_model = pickle.load(open(filename, 'rb'))
    #    return loaded_model
    filename = "knn_model.pkl"
    with open(filename, 'rb') as file:  
            Model = pickle.load(file)
    predict = st.button('PREDICT RANGE')
    if predict:
        
        pred = Model.predict(features2)
        if pred == 0 :
            st.write('Less than 3k')
        elif pred ==1:
            st.write('Between 3k to 4k')
        elif pred == 2:
            st.write('Between 4k to 5k')
        elif pred == 3:
            st.write('Between 5k to 6k')
        elif pred == 4:
            st.write('Between 6k to 7k')
        else :
            st.write('Above 7k')



if __name__ == "__main__":
    main()