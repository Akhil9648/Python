import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Bangalore House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# --------------------
# Load Artifacts
# --------------------
model = joblib.load("house_price_model.pkl")
locations = joblib.load("locations.pkl")

# --------------------
# Header Section
# --------------------
st.markdown(
    """
    <h1 style="text-align:center;">🏠 Bangalore House Price Prediction</h1>
    <p style="text-align:center; font-size:18px;">
    An end-to-end Machine Learning application to estimate real estate prices using data-driven intelligence.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# --------------------
# Layout
# --------------------
col1, col2 = st.columns(2)

with col1:
    total_sqft = st.number_input("Total Area (sqft)", min_value=300, max_value=10000, step=50)
    bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)

with col2:
    bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1)
    location = st.selectbox("Location", locations)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------
# Prediction
# --------------------
if st.button("🔮 Predict Price"):
    input_data = pd.DataFrame([{
        "total_sqft": total_sqft,
        "bath": bath,
        "bhk": bhk,
        "location": location
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ₹ {round(prediction, 2)} Lakhs")

# --------------------
# Footer
# --------------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray;">
    Built with ❤️ using Python, Scikit-learn and Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
