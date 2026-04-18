 💊 Medical Insurance Cost Prediction & Risk Segmentation

📌 Project Overview
This project predicts annual medical insurance costs using machine learning and segments customers into risk categories.

 🎯 Objective
- Predict healthcare costs
- Identify high-risk individuals
- Provide business recommendations for insurance pricing

## 📊 Dataset Features
- Demographics: age, sex, region, income
- Health: BMI, blood pressure, diabetes, etc.
- Insurance: premiums, claims, coverage
- Lifestyle: smoking, alcohol usage

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn, XGBoost
- Streamlit

## 🤖 Models Used
- Random Forest Regressor
- XGBoost Regressor

## 📈 Results
- Achieved strong R² score
- Accurate cost prediction
- Identified key drivers of cost

## 🔍 Key Insights
- Smokers have significantly higher costs
- BMI strongly influences medical expenses
- Chronic diseases increase insurance burden

## 💡 Business Recommendations
- Increase premiums for high-risk individuals
- Offer discounts for low-risk customers
- Promote preventive healthcare programs

## 🚀 How to Run

```bash
pip install -r requirements.txt
cd deployment
streamlit run app.py
