import streamlit as st 
def connect():
    st.markdown("""
    <div class="content-container2" style="margin-bottom: 50px;">
        <h1 class="custom-heading">Contact Information</h1>
        <br>    
    </div>
    
    <div style="text-align: center; display: flex; justify-content: center; gap: 20px; margin-top: 40px; margin-bottom: 40px;">
        <div style="margin-right: 20px;">
            <a href="https://www.linkedin.com/in/anandapadmanabhan-s-43959522a/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" alt="LinkedIn Profile" width="50">
            </a>
            <p style="font-family: 'Lora', sans-serif; font-size: 18px; margin-top: 10px;">LinkedIn</p>
        </div>
        <div style="margin-right: 20px;">
            <a href="mailto:anandapadmanabhan777@gmail.com">
                <img src="https://cdn-icons-png.flaticon.com/512/552/552486.png" alt="Email Me" width="50">
            </a>
            <p style="font-family: 'Lora', sans-serif; font-size: 18px; margin-top: 10px;">Email</p>
        </div>
        <div style="margin-right: 20px;">
            <a href="https://github.com/anandapadmanabhan-777" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub Profile" width="50">
            </a>
            <p style="font-family: 'Lora', sans-serif; font-size: 18px; margin-top: 10px;">GitHub</p>
        </div>
    </div>
    <div class="image-container2">
                <img src="https://github.com/anandapadmanabhan-777/JustAnImage/raw/main/JustAnImage.png" alt="Custom Image">
    </div>
    """, unsafe_allow_html=True)
