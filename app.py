import streamlit as st
import pickle
import numpy as np
import os

# Load the trained model
model_path = os.path.join('model', 'churn_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

st.title("📞 Telco Customer Churn Prediction")

st.markdown("""
Enter the customer's details below to predict whether they are likely to churn.
""")

# Layout: Using columns for inputs side-by-side
col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.number_input(
        'Tenure (months)', min_value=0, max_value=72, value=12,
        help='Number of months the customer has stayed with the company'
    )
with col2:
    monthly_charges = st.number_input(
        'Monthly Charges ($)', min_value=0.0, max_value=150.0, value=70.0, step=0.1,
        help='Customer’s monthly bill amount in USD'
    )
with col3:
    total_charges = st.number_input(
        'Total Charges ($)', min_value=0.0, max_value=10000.0, value=1500.0, step=1.0,
        help='Total amount billed to the customer so far in USD'
    )

st.markdown("---")

# Prediction button
if st.button('Predict Churn'):
    # Prepare input (make sure order matches your model training features)
    input_data = np.array([[tenure, monthly_charges, total_charges]])
    
    # Predict churn (0 = stay, 1 = churn)
    prediction = model.predict(input_data)[0]

    # Predict churn probability for class 1
    proba = model.predict_proba(input_data)[0][1]

    # Show probability nicely formatted
    st.write(f"### Churn Probability: {proba:.2%}")

    # Show message based on prediction
    if prediction == 1:
        st.error("⚠️ Customer is likely to churn 😟")
    else:
        st.success("✅ Customer is likely to stay 😊")
