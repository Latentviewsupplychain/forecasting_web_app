# -*- coding: utf-8 -*-
"""
created on mon jan 23 12:53:07 2023

@author: rishabh.gupta
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for prediction

def forecast_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    prediction = prediction.astype(int)
    prediction = prediction[0]
    print(prediction)
    
    
    return prediction


def main():
    
    # st.set_page_config(layout="wide")

    
    # giving a title
    st.title('Demand Forecasting Simulation')
    
    st.write("""
Simulate different scenarios by changing Markeing, Product and Economic Variables and predict the forecast.
""")
    # col1, col2, col3 = st.tabs(["cat", "dog", "owl"])
    
    # getting the input data from the user
    with st.expander("Product Variables (click to expand)"):

        option = st.multiselect("Select product category",['Hair care', 'Ice cream'])
        if 'Hair care' in option:
            st.write("""
         ### Product Id
         """)
            Key_cat = st.selectbox('Select Product Id',(202210
            ,202211,202212,202213,202214,202215,202216,202217,202218,202219,
             202225,202226,202227,202228,202229))

        else:
        
            Key_cat = st.selectbox('Select Product Id',(20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,202220,202221,202222,202223,202224,
            ))

        
        
        
        st.write("""
        ### cummulative sum
        """)
        cummulative_sum = st.slider('Sum all shipment quantity before the current week', value=5000, min_value=1000, max_value=14000, step=1000)
        
        st.write("""
        ### frequency
        """)
        frequency = st.slider('Frequency of non zero shipments', value=16, min_value=1, max_value=65 ,step=4)
        
        st.write("""
        ### recency
        """)
        recency = st.slider('Number of days since a non zero shipment', value=24, min_value=1, max_value=100 ,step=8)
        
        st.write("""
        ### previous shipment quantity
        """)
        previous_shipment_quantity = st.text_input('enter previous shipment quantity here',10)
        
        st.write("""
        ### weeks remaining to delist
        """)
        diff_delist_weeks = st.slider('select number of weeks remaining for a product to delist', value=16, min_value=1, max_value=65 ,step=4)


    with st.expander("Economic Variables (click to expand)"):
        st.write("""
        ### cpi natural gas
        """)
        cpi_natural_gas = st.slider('select consumer price index', value=30, min_value=0, max_value=50, step=5)
        
        
        st.write("""
        ### inflation
        """)
        inflation = st.text_input('enter inflation rate here',6)
        
        
        st.write("""
        ### civil unemployment
        """)
        civil_unemployment = st.text_input('enter civil unemployment',4)
        
        st.write("""
        ### cpi food at home
        """)
        cpi_food_at_home = st.slider('select consumer price index', value=10, min_value=0, max_value=20, step=2)
        
        st.write("""
        ### purchasing manager index
        """)
        pmi = st.slider('select pmi', value=57, min_value=0, max_value=100 ,step=10)
        
        
        st.write("""
        ### counsumer sentiment
        """)
        consumer_sentiment = st.slider('select consumer sentiment', value=40, min_value=10, max_value=100 ,step=10)
        
        st.write("""
        ### retail sales
        """)
        retail_sales = st.slider('select retail sales', value=550000, min_value=500000, max_value=620000, step=20000)
        st.write("""
        ### interest rate
        """)
        intrest_rate = st.slider('select interest rate', value=4, min_value=1, max_value=10, step=1)

                
        st.write("""
        ### cpi energy
        """)
        cpi_energy = st.slider('select consumer price index', value=30, min_value=20, max_value=40, step=2)
        
        

        
    with st.expander("Market Variables (click to expand)"):
        
        st.write("""
        ### cash discount per case off invoice
        """)
        cash_discount_per_case_off_invoice = st.text_input('enter cash discount here',0)

        

        st.write("""
        ### distributed promo quantity
        """)
        distributed_promo_qty = st.text_input('enter distributed promo quantity here',10)
        
        st.write("""
        ### holiday count
        """)
        holiday_count = st.text_input('enter number of holidays here',2)
        
        st.write("""
        ### month end
        """)
        month_end = st.text_input("enter 1 if it is a month end otherwise 0",0)

        st.write("""
        ### quarter end
        """)
        qrt_end = st.text_input("enter 1 if it is a quarter end otherwise 0",0)
        
        st.write("""
        ### penetration tpr
        """)
        penetration_tpr = st.text_input('enter penetration tpr value',0)
    
    # code for prediction
    forecast = ''
    
    # creating a button for prediction
    
    if st.button('Predict Forecast'):
        forecast = forecast_prediction([Key_cat,cummulative_sum, frequency, previous_shipment_quantity, diff_delist_weeks, recency, pmi, consumer_sentiment, distributed_promo_qty,holiday_count,intrest_rate,cash_discount_per_case_off_invoice,retail_sales,month_end,cpi_natural_gas,inflation,civil_unemployment,qrt_end,cpi_food_at_home,penetration_tpr,cpi_energy])
      
    
        
    st.success(forecast)
    
    
    
    
if __name__ == '__main__':
    main()