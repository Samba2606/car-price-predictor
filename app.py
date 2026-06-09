import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model
model = pickle.load(open('cpmodel.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# Header
st.title("🚗 Car Price Predictor")
st.caption("Enter car details below to predict the market price.")
st.divider()

st.markdown("### 📋 Enter Car Details")

# Load data for dropdown options
cars_df = pd.read_csv('cleaned_car.csv')

# Input fields
company = st.selectbox("Car Company", sorted(cars_df['company'].unique()))
name = st.selectbox("Car Model", sorted(cars_df[cars_df['company'] == company]['name'].unique()))
year = st.selectbox("Year of Purchase", sorted(cars_df['year'].unique(), reverse=True))
kms_driven = st.slider("Kilometres Driven", 0, 500000, 50000, step=1000)
fuel_type = st.selectbox("Fuel Type", cars_df['fuel_type'].unique())

st.divider()

# Predict button
if st.button("🔍 Predict Car Price", use_container_width=True):
    input_data = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    prediction = model.predict(input_data)
    price = prediction[0]

    st.success(f"💰 Estimated Market Price: ₹ {price:,.0f}")
    st.markdown(f"""
    **Car Details:**
    - Model: {name}
    - Company: {company}
    - Year: {year}
    - Kilometres Driven: {kms_driven:,} km
    - Fuel Type: {fuel_type}
    """)

st.divider()
st.caption("Built by Tankala Samba Siva Mani · Powered by Machine Learning · Accuracy: 90%+")