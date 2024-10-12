import pickle
import joblib
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('app.py', 'w') as f:
    model = joblib.load(model_file)

st.title('Laptop CPU Frequency Predictor App')

# Add input widgets for user inputs
company = st.selectbox(
    "Company",
  ["Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba", "Apple", "Samsung", "Razer", "Mediacom", "Microsoft", "Xiaomi",
"Vero", "Chuwi", "Google", "Fujitsu", "LG", "Huawei"]
)
primary_storage = st.slider("PrimaryStorage", min_value=8.0, max_value=2048.0, value=256.0)
inches = st.slider("Inches", min_value=10.1, max_value=18.4, value=15.6)
ram = st.slider("Ram", min_value=2.0, max_value=64.0, value=8.0)
# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
    input_data = pd.DataFrame({
        'Company': [company],
        'PrimaryStorage': [primary_storage],
        'Inches': [inches],
        'Ram': [ram]
    })
    prediction = model.predict(input_data)[0].round(1)
    st.write(f'The predicted value is: {prediction}') 
