import streamlit as st

def about():
    st.markdown(
    """
    <div class="content-container2">
        <h1 class="custom-heading">About Me</h1>
    </div>
    <div>
        <h3 class="custom-lines2"><br>Aspiring AI/ML Engineer 💻🧠 &nbsp; | &nbsp; Python Developer 🐍 &nbsp; | &nbsp; Full Stack Python Developer 🕸️</h3>
        <h1 class="custom-heading2">EDUCATION</h1>
        <h3 class="custom-lines3"> &nbsp; ● BTech in Infomation Technology<br> &nbsp; ● Diploma in Computer Engineering</h3>
    </div>
    """,
    unsafe_allow_html=True,
)
