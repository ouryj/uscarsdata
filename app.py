#importing necessary packages to run the app
import pandas as pd
import streamlit as st
import plotly_express as px
import numpy as np

# laoding the datset
df = pd.read_csv('vehicles_us.csv')

#setting the header for the application
st.header("US Used Cars Visualization")
# Calculating lower and upper bound for the outliers
lower = df['price'].quantile(0.5)
upper = df['price'].quantile(0.95)
# setting a checkbox fo excluding the outliers
exclude_outliers = st.checkbox("Disregard outliers")
#condition to exclude outliers
if exclude_outliers:
    filtered_df = df[(df['price'] >= lower) & (df['price'] <= upper)]

else:
    filtered_df = df

#creating a histogram
hist = px.histogram(filtered_df, x='price', title='Used Cars Price Distribution')
#displaying the histogram via streamlit
if st.checkbox("view histogram chart"):
    st.plotly_chart(hist)

#creating a scatterplot for price vs odometer
scatter = px.scatter(filtered_df, x='price', y='odometer',title='Relationship btw Price & Mileage', labels={'price':'USD $$', 'odometer': 'Miles'}
                     )
#displaying the scatterplot
if st.checkbox("view relationship btw Price & Miles"):
    st.plotly_chart(scatter)

#check box for raw data
if st.checkbox('View Raw Data'):
    st.write(filtered_df)

#run app on the terminal by run streamlit run app.py
#     
