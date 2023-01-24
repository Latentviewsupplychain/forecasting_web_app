# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:53:07 2023

@author: rishabh.gupta
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def forecast_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    
    return prediction

  
    
  
def main():
    
    
    # giving a title
    st.title('Demand Forecasting Web App')
    
    st.write("""
This app predicts your future forecasts. Just fill in the following information and click on the Predict button.
""")
    
    
    # getting the input data from the user

    st.write("""
    ### Cummulative Sum
    """)
    Cummulative_sum = st.slider('Select commulative sum', value=5000, min_value=1000, max_value=14000, step=1000)
    
    st.write("""
    ### Frequency
    """)
    Frequency = st.slider('Select frequency', value=16, min_value=1, max_value=65 ,step=4)
    
    
    st.write("""
    ### Previous Shipment Quantity
    """)
    Previous_shipment_quantity = st.text_input('Enter previous shipment quantity here')
    
    st.write("""
    ### diff_delist_weeks
    """)
    diff_delist_weeks = st.slider('Select difference in delist weeks', value=16, min_value=1, max_value=65 ,step=4)
    
    
    st.write("""
    ### Recency
    """)
    Recency = st.slider('Select recency', value=24, min_value=1, max_value=100 ,step=8)
    
    st.write("""
    ### Purchasing Manager Index
    """)
    pmi = st.slider('Select pmi', value=57, min_value=55, max_value=60 ,step=1)
    
    
    st.write("""
    ### Counsumer Sentiment
    """)
    consumer_sentiment = st.slider('Select consumer sentiment', value=58, min_value=50, max_value=68 ,step=2)
    
    
    st.write("""
    ### Distributed Promo Quantity
    """)
    Distributed_Promo_QTY = st.text_input('Enter distributed promo quantity here',10)
    
    st.write("""
    ### Holiday Count
    """)
    holiday_count = st.text_input('Enter number of holidays here',2)
    
    
    st.write("""
    ### Interest Rate
    """)
    intrest_rate = st.slider('Select interest rate', value=4, min_value=2, max_value=9, step=1)
    
    
    
    st.write("""
    ### Cash Discount Per Case Off Invoice
    """)
    Cash_Discount_Per_Case_Off_Invoice = st.text_input('Enter cash discount here',0)
    
    
    st.write("""
    ### Retail Sales
    """)
    retail_sales = st.slider('Select consumer sentiment', value=550000, min_value=500000, max_value=620000, step=20000)
    
    st.write("""
    ### Month End
    """)
    Month_End = st.text_input("Enter 1 if it is a month end otherwise 0")
    
    
    
    st.write("""
    ### cpi natural gas
    """)
    cpi_natural_gas = st.slider('Select cpi', value=30, min_value=20, max_value=38, step=2)
    
    
    st.write("""
    ### Inflation
    """)
    inflation = st.text_input('Enter inflation rate here',8)
    
    
    st.write("""
    ### Civil Unemployment
    """)
    civil_unemployment = st.text_input('Enter civil unemployment',4)
    
    st.write("""
    ### Quarter End
    """)
    Qrt_End = st.text_input("Enter 1 if it is a quarter end otherwise 0")
    
    st.write("""
    ### Cpi food at home
    """)
    cpi_food_at_home = st.slider('Select cpi', value=10, min_value=0, max_value=20, step=2)
    
    
    st.write("""
    ### Penetration TPR
    """)
    Penetration_TPR = st.text_input('Enter Penetration TPR value',0)
    
    st.write("""
    ### Cpi Energy
    """)
    cpi_energy = st.slider('Select cpi', value=30, min_value=20, max_value=40, step=2)
    
    
    
    
    # code for Prediction
    Forecast = ''
    
    # creating a button for Prediction
    
    if st.button('Forecast Test Result'):
        Forecast = forecast_prediction([Cummulative_sum, Frequency, Previous_shipment_quantity, diff_delist_weeks, Recency, pmi, consumer_sentiment, Distributed_Promo_QTY,holiday_count,intrest_rate,Cash_Discount_Per_Case_Off_Invoice,retail_sales,Month_End,cpi_natural_gas,inflation,civil_unemployment,Qrt_End,cpi_food_at_home,Penetration_TPR,cpi_energy])
        
        
    st.success(Forecast)
    
    
    
    
    
if __name__ == '__main__':
    main()