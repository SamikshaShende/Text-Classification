import streamlit as st 
import joblib

model = joblib.load('model.joblib')
st.set_page_config(page_title="Flight Review Analyzer", page_icon="✈️", layout="centered")
st.title("Flight Review Analyzer")
st.subheader("Enter your flight review below:")

review = st.text_area("Review", height=200)
st.write("Click the button to analyze the review.")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review before analyzing.")
    else:
        prediction = model.predict([review])
        st.write(f"Prediction: {prediction[0]}")
