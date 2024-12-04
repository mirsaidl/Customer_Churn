import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model and preprocessing pipeline
log_reg = joblib.load('log_reg.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Set up the Streamlit app
st.title("Customer Churn Prediction")

## add image to the app

st.image('assets/image.png', width=700)

# Collect user input on the main interface
st.header("Enter Customer Details")

# Input fields for each column
customer_id = st.text_input("Customer ID")
age = st.slider("Age", 18, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.slider("Tenure (months)", 0, 60, 12)
usage_frequency = st.slider("Usage Frequency (times/month)", 1, 100, 10)
support_calls = st.slider("Number of Support Calls", 0, 20, 2)
payment_delay = st.slider("Payment Delay (days)", 0, 30, 5)
subscription_type = st.selectbox("Subscription Type", ["Basic", "Premium", "VIP"])
contract_length = st.selectbox("Contract Length (months)", ["Quarterly", "Monthly", "Annual"])
total_spend = st.number_input("Total Spend ($)", min_value=0.0, step=0.1, format="%.2f")
last_interaction = st.number_input("Last Interaction (days ago)", min_value=0, step=1, format="%d")

# Check if all required fields are filled and submit button is pressed
if st.button("Submit"):
    if not customer_id or total_spend <= 0 or last_interaction < 0:
        st.warning("Please fill out all required fields.")
    else:
        # Prepare the input data for the model
        input_data = pd.DataFrame({
            'CustomerID': [customer_id],
            'Age': [age],
            'Gender': [gender],
            'Tenure': [tenure],
            'Usage Frequency': [usage_frequency],
            'Support Calls': [support_calls],
            'Payment Delay': [payment_delay],
            'Subscription Type': [subscription_type],
            'Contract Length': [contract_length],
            'Total Spend': [total_spend],
            'Last Interaction': [last_interaction]
        })

        # Preprocess the input data using the loaded preprocessor
        input_data_preprocessed = preprocessor.transform(input_data)

        # Make predictions
        y_pred = log_reg.predict(input_data_preprocessed)

        # Display the prediction
        st.header("Prediction Result")
        if y_pred[0] == 1.0:
            st.error("The customer is likely to churn.")
        else:
            st.success("The customer is not likely to churn.")
