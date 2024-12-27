import streamlit as st
import fashion_page as fa
import mnist_page as mn
import fraud_page as fr
import churn_page as ch

def projects():
    # Initialize session state for navigation
    if "selected_project" not in st.session_state:
        st.session_state.selected_project = "None"
        

    # Main Projects Page
    if st.session_state.selected_project == "None":
        
        st.markdown("""
            <div class="content-container2">
                <h1 class="custom-heading">AI/ML Projects</h1>
            </div>
            <br>
            """, unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Customer Churn Prediction"):
                st.session_state.selected_project = "Customer Churn"
                st.rerun()
        with col2:
            if st.button("Credit Card Fraud Detection"):
                st.session_state.selected_project = "Credit Card Fraud"
                st.rerun()
        with col3:
            if st.button("MNIST Digit Recognizer"):
                st.session_state.selected_project = "MNIST"
                st.rerun()
        with col4:
            if st.button("Fashion-MNIST"):
                st.session_state.selected_project = "Fashion-MNIST"
                st.rerun()

    # Render Specific Project Page
    elif st.session_state.selected_project == "Customer Churn":
        ch.churn_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "Credit Card Fraud":
        fr.fraud_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "MNIST":
        mn.mnist_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()

    elif st.session_state.selected_project == "Fashion-MNIST":
        fa.fashion_page()
        if st.button("Back to Projects"):
            st.session_state.selected_project = "None"
            st.rerun()
            