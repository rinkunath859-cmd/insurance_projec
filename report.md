
Medical Insurance Cost Prediction & Risk Segmentation
1. Executive Summary

This project focuses on predicting annual medical insurance costs using machine learning and identifying high-risk customer segments. The model analyzes demographic, lifestyle, medical, and insurance-related factors to estimate healthcare expenses.

The results show that factors such as smoking, BMI, chronic diseases, and healthcare utilization significantly impact medical costs. The project helps insurance companies improve pricing strategies, reduce risk, and design better customer-focused policies.

2. Business Problem

Insurance companies face challenges in accurately predicting medical costs.

Underestimation leads to financial losses
Overestimation reduces competitiveness
Lack of risk segmentation affects decision-making

A data-driven approach is required to improve pricing, manage risk, and optimize customer strategies.

3. Objectives

The key objectives of this project are:

Predict annual medical insurance cost
Identify major cost-driving factors
Segment customers based on risk
Provide actionable business recommendations
4. Dataset Overview

The dataset contains detailed customer information, including:

Demographics: age, sex, region, income
Health metrics: BMI, blood pressure, HbA1c, LDL
Lifestyle factors: smoking, alcohol consumption
Medical history: chronic diseases
Insurance details: plan type, deductible, policy term
Healthcare usage: claims, visits, hospitalizations
Target variable: annual medical cost

This dataset enables both prediction and business insight generation.

5. Methodology

The project followed a complete data science workflow:

Data loading and cleaning
Handling missing values
Encoding categorical variables
Feature scaling
Train-test split
Model training (Random Forest)
Model evaluation (RMSE, R²)
Deployment using Streamlit
6. Model Performance

The model achieved good prediction performance:

RMSE indicates acceptable prediction error
R² score shows strong explanatory power

This confirms that medical costs can be effectively predicted using available features.

7. Key Findings

The analysis revealed the following:

Smoking significantly increases medical costs
Higher BMI leads to higher healthcare expenses
Chronic diseases strongly impact insurance claims
Increased hospital visits and procedures raise costs
A small group of high-risk customers contributes most to total expenses
8. Business Insights
Risk Concentration

High-risk customers account for a large portion of total medical costs.

Lifestyle Impact

Smoking and obesity are major cost drivers and are preventable.

Cost Drivers

Medical utilization (claims, hospitalizations) strongly influences expenses.

Segmentation Opportunity

Customers can be grouped into low, medium, and high-risk categories.

9. Recommendations
1. Risk-Based Pricing

Adjust premiums based on predicted medical risk.

2. Preventive Healthcare Programs

Introduce programs for smoking cessation and weight management.

3. High-Risk Customer Monitoring

Closely track high-risk individuals to reduce future claims.

4. Low-Risk Customer Retention

Offer discounts and benefits to low-risk customers.

5. Data-Driven Decision Making

Use predictive models in underwriting and pricing strategies.

10. Deployment

A Streamlit web application was developed where users can:

Enter customer details
Predict medical cost instantly

This demonstrates real-world applicability of the model.

11. Business Value

This project provides:

Improved pricing accuracy
Better risk management
Identification of cost-saving opportunities
Enhanced customer targeting strategies
12. Limitations
Model depends on data quality
External factors like inflation not included
Deployment is a prototype, not production-ready
13. Future Scope
Use advanced models like XGBoost
Add explainability (SHAP)
Improve risk segmentation
Deploy on cloud platforms
Monitor model performance over time
14. Conclusion

This project demonstrates how machine learning can solve real-world insurance problems. It enables accurate cost prediction, better risk segmentation, and improved business decision-making.

The approach can help insurance companies enhance profitability while providing fair and efficient pricing to customers.
