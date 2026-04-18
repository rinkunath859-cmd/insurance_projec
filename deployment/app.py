import streamlit as st
import pandas as pd
import pickle

# ==============================
# LOAD FILES
# ==============================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("💊 Medical Insurance Cost Prediction")

st.write("Enter details below to predict medical cost")

# ==============================
# USER INPUTS
# ==============================
age = st.slider("Age", 18, 80, 30)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
income = st.number_input("Income", value=50000)
children = st.slider("Children", 0, 10, 1)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

# ==============================
# CREATE INPUT DATA
# ==============================
input_dict = {
    "age": age,
    "bmi": bmi,
    "income": income,
    "children": children,
    "sex": sex,
    "smoker": smoker,
    "region": region
}

input_df = pd.DataFrame([input_dict])

# ==============================
# ENCODING
# ==============================
input_df = pd.get_dummies(input_df)

# Match training columns
input_df = input_df.reindex(columns=columns, fill_value=0)

# ==============================
# SCALING
# ==============================
input_scaled = scaler.transform(input_df)

# ==============================
# PREDICTION
# ==============================
if st.button("Predict Cost"):
    prediction = model.predict(input_scaled)
    st.success(f"Estimated Medical Cost: ₹ {prediction[0]:,.2f}")