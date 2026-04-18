# 💊 Medical Insurance Cost Prediction & Risk Segmentation

## 📌 Project Overview
This project predicts annual medical insurance costs using machine learning and segments customers into risk categories. It helps insurance companies improve pricing, risk management, and customer strategy using data-driven insights.




---

## 🎯 Objectives
- Predict annual medical insurance cost
- Identify key cost-driving factors
- Segment customers into risk groups
- Provide actionable business recommendations

---

## 📊 Dataset Overview
The dataset contains:

- **Demographics**: age, sex, region, income  
- **Health Metrics**: BMI, blood pressure, HbA1c  
- **Lifestyle Factors**: smoking, alcohol usage  
- **Medical History**: chronic diseases  
- **Insurance Details**: plan type, deductible  
- **Healthcare Usage**: visits, claims, hospitalizations  
- **Target Variable**: annual medical cost  

---

## 🔍 Exploratory Data Analysis (EDA)

### Distribution of Medical Cost
![EDA Plot]
<img width="690" height="487" alt="distribution of ,edical cost" src="https://github.com/user-attachments/assets/6e5fbccc-b56d-4351-aedf-770a62230032" />
<img width="906" height="697" alt="correlation heatmap" src="https://github.com/user-attachments/assets/93062199-806c-44f9-a324-9282f4f03524" />
<img width="697" height="485" alt="BMI VS Medical cost" src="https://github.com/user-attachments/assets/03cd3c8e-b9ba-4dc8-b7f6-55e2fcd9a654" />
<img width="700" height="490" alt="Age VS Medical cost" src="https://github.com/user-attachments/assets/2aeb64c3-64b2-401e-856f-2b09ec995491" />



**Insight:**
- Medical cost is right-skewed
- Few high-cost individuals contribute significantly

---

### Feature Importance
![Feature Importance]
<img width="933" height="520" alt="feature_importance" src="https://github.com/user-attachments/assets/76db5ea9-e761-48d2-9cdf-6039732bf5a6" />


**Insight:**
- Smoking, BMI, and age are key cost drivers
- Lifestyle and health factors strongly impact cost

---

## ⚙️ How It Works
1. User enters details in Streamlit app  
2. Data is preprocessed and scaled  
3. Model predicts medical cost  
4. Output is displayed instantly  

---

## 🤖 Models Used
- Random Forest Regressor  
- XGBoost Regressor  

---

## 📈 Key Results
- R² Score: High predictive accuracy  
- Low RMSE indicating reliable predictions  
- Model successfully identifies cost patterns  

---

## 📸 Prediction Output

![Prediction]
<img width="972" height="915" alt="Prediction result" src="https://github.com/user-attachments/assets/3020ec99-4105-4656-9a0c-af9c45f21654" />


---

## 🧠 Key Insights
- Smokers have significantly higher medical costs  
- Higher BMI leads to increased healthcare expenses  
- Chronic diseases strongly impact insurance claims  
- High-risk individuals contribute most to total cost  

---

## 💡 Business Recommendations
- Implement risk-based pricing strategies  
- Promote preventive healthcare programs  
- Monitor high-risk customers closely  
- Offer incentives to low-risk customers  

---

## 🌍 Business Impact
This project helps insurance companies to:
- Improve pricing accuracy  
- Reduce financial risk  
- Identify high-cost customers  
- Enhance decision-making  

---

## 🚀 How to Run the Project

```bash
pip install -r requirements.txt
cd deployment
streamlit run app.py
