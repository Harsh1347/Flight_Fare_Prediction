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
    filename = "model.pkl"
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
    st.bar_chart([7129.404287901991,
 6437.2867860970755,
 5925.805196778605,
 5628.013529948313,
 5373.616189176899,
 5154.125416036309,
 4977.196199668225,
 4885.456663137195,
 4727.410427402243,
 4697.983502345996,
 4654.95372477621,
 4600.623186215235,
 4510.130593607306,
 4433.4427988514435,
 4343.698908429351,
 4355.696344607917,
 4416.950531107739,
 4399.727662178702,
 4389.83721633888,
 4396.037818955043,
 4409.618997281788,
 4420.793332327651,
 4452.35712130356,
 4474.380054315027,
 4511.4169568508705,
 4523.580450219067,
 4552.522816560894,
 4542.579963789982,
 4593.347071256038,
 4612.299939375568,
 4601.979641079777,
 4600.861505896583,
 4636.62893939394,
 4617.976021716182,
 4571.463752825923,
 4574.844633627243,
 4612.220269656113,
 4654.692716236722,
 4612.1050097788475,
 4581.128866757205,
 4608.339477262426,
 4653.57052154195,
 4652.873735085334,
 4607.811855670103,
 4583.501137915339,
 4606.298352654057,
 4691.361174156454,
 4709.8155931171,
 4723.065623575877,
 4716.514993880049,
 4710.8766641162965,
 4737.53689335159,
 4746.5858260469395,
 4771.86342133374,
 4762.27731092437,
 4739.138496932515,
 4754.853506097561,
 4768.623183973084,
 4742.511770100887,
 4727.002764127764,
 4718.490297937356,
 4687.106121193479,
 4681.08480024491,
 4697.832209623046,
 4688.727856815053,
 4679.2226794695935,
 4642.553488372093,
 4658.100030543677,
 4695.07216022015,
 4733.770344407193,
 4711.448281130634,
 4705.32605709052,
 4729.6009461315425,
 4750.834756097561,
 4772.588020674977,
 4756.91196698762,
 4787.1418126428025,
 4793.57620647526,
 4792.216806722689,
 4771.364176829268,
 4765.682699648802,
 4777.744535519126,
 4756.697599755389,
 4751.170409711684,
 4708.690097799511,
 4716.568001222494,
 4698.170527278269,
 4654.1166590319135,
 4639.192958390489,
 4590.580404685836,
 4550.8691688193285,
 4515.405620036652,
 4522.994214372716])



if __name__ == "__main__":
    main()
