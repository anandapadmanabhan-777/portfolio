import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np


def fashion_page():
    st.markdown(
        """
        
            <h1 class="custom-heading2">Fashion-MNIST Classifier</h1>
            <h3 class="custom-subheader">Fashion MNIST Model Loaded..!!</h3>
            <h3 class="custom-subheader">Upload an image of a fashion item to classify it.</h3>
        """,
        unsafe_allow_html=True,
    )
    fashion_mnist_model = load_model('models/fashion_mnist_model.keras')
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image = image.convert('L')  # Convert to grayscale
        image = image.resize((28, 28))  # Resize to 28x28 for Fashion-MNIST
        image = np.array(image) / 255.0  # Normalize the image
        image = image.reshape(1, 28, 28, 1)  # Reshape for model input
        class_labels = [
            "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
            "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
        ]
        if st.button("Predict Fashion Item"):
            prediction = fashion_mnist_model.predict(image)
            predicted_label = np.argmax(prediction)
            predicted_class = class_labels[predicted_label]
            st.write("Predicted Fashion Item:", predicted_class)
