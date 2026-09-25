import streamlit as st
import numpy as np
import sklearn
from sklearn.tree import DecisionTreeClassifier

# Page title
st.title("Titanic Survival Prediction App")
st.write("Deploy your trained model into a simple interactive web app with input sliders and real-time prediction output.")

# User input sliders and controls
st.sidebar.header("User Input Parameters")
pclass = st.sidebar.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.slider("Age", 1, 80, 25)
fare = st.sidebar.slider("Fare (£)", 0.0, 500.0, 32.0)

# Convert categorical input to numerical
sex_val = 0 if sex == "Male" else 1

# Mock/Trained Prediction Logic (or load using joblib/pickle if you saved a model)
# model = joblib.load('model.pkl')
# prediction = model.predict([[pclass, sex_val, age, fare]])

# For demo purposes, a simple rule-based estimator matching the decision tree concept:
is_survived = True if (sex_val == 1 or (pclass == 1 and age < 40)) else False

st.subheader("Prediction Result")
if st.button("Predict Survival"):
    if is_survived:
        st.success("The model predicts: **Survived** 🎉")
    else:
        st.error("The model predicts: **Did Not Survive** ⚠️")
