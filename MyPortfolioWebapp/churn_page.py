import streamlit as st
import pandas as pd
import os
from keras.models import load_model

def churn_page():
    st.markdown(
        """
        
            <h1 class="custom-heading2">Customer Churn Prediction</h1>
            <h3 class="custom-subheader">Customer Churn Model Loaded..!!</h3>
            <h3 class="custom-subheader">Fill out the form below to predict whether a customer will churn or not.</h3>
        """,
        unsafe_allow_html=True,
    )
    # Get the absolute path to the models folder
    st.write(f"Model path: {model_path}")
    model_path = os.path.join(os.getcwd(), "models", "churn_model.keras")

    # Load the model
    churn_model = load_model(model_path)
    # churn_model = load_model('models/churn_model.keras')
    # Input form
    with st.form("churn_form"):
        # Categorical Inputs
        gender = st.selectbox("Gender", options=["Male", "Female"])
        geography = st.selectbox("Geography", options=["France", "Germany", "Spain"])
        has_cr_card = st.radio("Has Credit Card?", options=["Yes", "No"])
        is_active_member = st.radio("Is Active Member?", options=["Yes", "No"])

        # Continuous Inputs
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, step=1)
        balance = st.number_input("Balance (in $)", min_value=0.0, step=100.0)
        num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, step=1)
        estimated_salary = st.number_input("Estimated Salary (in $)", min_value=0.0, step=100.0)

        # Submit button
        submitted = st.form_submit_button("Predict Churn")

    if submitted:
        # Encode categorical inputs
        gender_encoded = 1 if gender == "Male" else 0
        has_cr_card_encoded = 1 if has_cr_card == "Yes" else 0
        is_active_member_encoded = 1 if is_active_member == "Yes" else 0

        # One-hot encode 'Geography'
        geography_germany = 1 if geography == "Germany" else 0
        geography_spain = 1 if geography == "Spain" else 0

        # Create input DataFrame with one-hot encoded columns for Geography
        input_data = pd.DataFrame({
            "CreditScore": [credit_score],
            "Gender": [gender_encoded],
            "Age": [age],
            "Tenure": [tenure],
            "Balance": [balance],
            "NumOfProducts": [num_of_products],
            "HasCrCard": [has_cr_card_encoded],
            "IsActiveMember": [is_active_member_encoded],
            "EstimatedSalary": [estimated_salary],
            "Geography_Germany": [geography_germany],
            "Geography_Spain": [geography_spain]
        })

        # Ensure the order of columns matches the model's training data
        expected_columns = [
            "CreditScore", "Gender", "Age", "Tenure", "Balance", "NumOfProducts",
            "HasCrCard", "IsActiveMember", "EstimatedSalary", "Geography_Germany", "Geography_Spain"
        ]
        input_data = input_data[expected_columns]

        # Make prediction
        prediction = churn_model.predict(input_data)
        result = "Customer will churn." if prediction[0][0] > 0.5 else "Customer will not churn."

        # Display result
        st.subheader(result)
