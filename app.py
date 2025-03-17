
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("customer_segmentation_model.pkl")

st.title("Customer Segmentation Predictor")

# Input fields
income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
spending = st.number_input("Spending Score (1-100)", min_value=0, max_value=100, value=50)

# Prediction
if st.button("Predict Segment"):
    df = pd.DataFrame([[income, spending]], columns=["Annual Income (k$)", "Spending Score (1-100)"])
    cluster = model.predict(df)
    st.success(f"Predicted Customer Segment: {cluster[0]}")
