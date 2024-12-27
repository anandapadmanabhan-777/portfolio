# import streamlit as st
# from keras.models import load_model
# import pandas as pd

# def fraud_page():
#     st.markdown(
#         """
        
#             <h1 class="custom-heading2">Credit Card Fraud Detection</h1>
#             <h3 class="custom-subheader">Fraud Detection Model Loaded..!!</h3>
#             <h3 class="custom-subheader">Upload a CSV file with transaction data to detect fraud.</h3>
#         """,
#         unsafe_allow_html=True,
#     )
#     fraud_model = load_model('models/fraud_model.keras')
#     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#     if uploaded_file is not None:
#         data = pd.read_csv(uploaded_file)
#         st.write(data.head())
#         if st.button("Predict Fraud"):
#             prediction = fraud_model.predict(data)
#             st.write("Prediction:", prediction)
#END


import streamlit as st
import pandas as pd
from keras.models import load_model

def fraud_page():
    st.markdown(
        """
            <h1 class="custom-heading2">Credit Card Fraud Detection</h1>
            <h3 class="custom-subheader">Fraud Detection Model Loaded..!!</h3>
            <h3 class="custom-subheader">Fill out the form below to predict whether a transaction is fraudulent or not.</h3>
        """,
        unsafe_allow_html=True,
    )
    fraud_model = load_model('models/fraud_model.keras')

    # Input form
    with st.form("fraud_form"):
        # Transaction Inputs
        transaction_id = st.number_input("Transaction ID", min_value=1)
        amount = st.number_input("Amount", min_value=0.0, step=1.0)
        merchant_id = st.number_input("Merchant ID", min_value=1)
        transaction_type = st.selectbox("Transaction Type", options=["Refund", "Purchase"])
        
        # Date Inputs (for TransactionDate encoding)
        year = st.number_input("Year", min_value=2000, max_value=2100, step=1)
        month = st.number_input("Month", min_value=1, max_value=12, step=1)
        day = st.number_input("Day", min_value=1, max_value=31, step=1)
        hour = st.number_input("Hour", min_value=0, max_value=23, step=1)

        # Submit button
        submitted = st.form_submit_button("Predict Fraud")

    if submitted:
        # Encode categorical inputs
        transaction_type_encoded = 1 if transaction_type == "Purchase" else 0

        # Create input DataFrame with encoded columns
        input_data = pd.DataFrame({
            "TransactionID": [transaction_id],
            "Amount": [amount],
            "MerchantID": [merchant_id],
            "TransactionType": [transaction_type_encoded],
            "Year": [year],
            "Month": [month],
            "Day": [day],
            "Hour": [hour]
        })

        # Ensure the order of columns matches the model's training data
        expected_columns = [
            "TransactionID", "Amount", "MerchantID", "TransactionType",
            "Year", "Month", "Day", "Hour"
        ]
        input_data = input_data[expected_columns]

        # Make prediction
        prediction = fraud_model.predict(input_data)
        result = "Fraudulent Transaction" if prediction[0][0] > 0.5 else "Non-Fraudulent Transaction"

        # Display result
        st.subheader(result)
