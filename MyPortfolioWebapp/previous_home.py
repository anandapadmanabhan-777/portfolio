import streamlit as st
def home():
    # Content inside the div
    st.markdown("""
    <div class="content-container">
        <h1 class="custom-heading">Welcome to My AI Portfolio..!!</h1>
        <p class="custom-paragraph">Here is some information about my AI portfolio, projects & skills: </p>
        <ul class="custom-list">
            <li class="custom-list-item">Project 1: AI-based Chatbot</li>
            <li class="custom-list-item">Project 2: Computer Vision Application</li>
            <li class="custom-list-item">Skills: Machine Learning, Deep Learning, NLP, Python</li>
        </ul>
     </div>   
    """, unsafe_allow_html=True)
    