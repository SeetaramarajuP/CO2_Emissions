# -*- coding: utf-8 -*-
"""emissions_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U0fWcdRpFHYd9MFK80AnY1H_Gooqcf_D
"""

import pandas as pd
import streamlit as st
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Set the title for your Streamlit app
st.title('Prediction Of CO2 Emissions')

# Create a sidebar for input features
st.sidebar.header('Input Features')

# Define a function to collect user input features
def input_features():
  Cylinders=st.sidebar.selectbox('Select No of Cylinders',('3','4','5','6','8','10','12','16'))

  MPG=st.sidebar.number_input('Insert The Miles Per Gallon')

  transmission_A=st.sidebar.selectbox('Automatic Transmission (A)',('0','1'))
  transmission_AM=st.sidebar.selectbox('Automated Manual Transmission (AM)',('0','1'))
  transmission_AS=st.sidebar.selectbox('Automatic with Select Shift Transmission (AS)',('0','1'))
  transmission_AV=st.sidebar.selectbox('Continuously Variable Transmission (AV)',('0','1'))
  transmission_M=st.sidebar.selectbox('Manual Transmission (M)',('0','1'))

  fuel_type_D=st.sidebar.selectbox('Fuel Type Diesel (D)',('0','1'))
  fuel_type_E=st.sidebar.selectbox('Fuel Type Ethanol (E)',('0','1'))
  fuel_type_N=st.sidebar.selectbox('Fuel Type Natural Gas (N)',('0','1'))
  fuel_type_X=st.sidebar.selectbox('Fuel Type Regular Gasoline (X)',('0','1'))
  fuel_type_Z=st.sidebar.selectbox('Fuel Type Premium Gasoline (Z)',('0','1'))

  data={'Cylinders':Cylinders,
              'Miles Per Gallon':MPG,
              'Automatic Transmission':transmission_A,
              'Automated Manual Transmission':transmission_AM,
              'Automatic with Selective Shift Transmission':transmission_AS,
              'Continuously Varaiable Transmission':transmission_AV,
              'Manual Transmission':transmission_M,
              'Fuel Type Diesel':fuel_type_D,
              'Fuel Type Ethanol':fuel_type_E,
              'Fuel Type Natural Gas':fuel_type_N,
              'Fuel Type Normal Gasoline':fuel_type_X,
              'Fuel Type Premium Gasoline':fuel_type_Z}

              # Create a DataFrame with the user input data

  features=pd.DataFrame(data,index=[0])
  return features
# Call the input_features() function to collect user input
df=input_features()

# Display the user input features as a subheader and a DataFrame
st.subheader('User Input Features')
st.write(df)

st.subheader('Prediction Result')

if st.button("Predict"):
    if input_features:
        # Make predictions using the loaded model
        predictions = model.predict(df)
        st.write(predictions)