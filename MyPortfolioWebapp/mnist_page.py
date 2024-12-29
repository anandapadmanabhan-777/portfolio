import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

def mnist_page():
    st.markdown(
        """
        
            <h1 class="custom-heading2">MNIST Digit Recognizer</h1>
            <h3 class="custom-subheader">MNIST Model Loaded..!!</h3>
            <h3 class="custom-subheader">Upload an image of a handwritten digit (0-9) for classification.</h3>
        """,
        unsafe_allow_html=True,
    )
    mnist_model = load_model('models/mnist_model.keras')
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image = image.convert('L')  # Convert to grayscale
        image = image.resize((28, 28))  # Resize to 28x28 for MNIST
        image = np.array(image) / 255.0  # Normalize the image
        image = image.reshape(1, 28, 28, 1)  # Reshape for model input
        if st.button("Predict Digit"):
            prediction = mnist_model.predict(image)
            st.write("Predicted Digit:", np.argmax(prediction))
