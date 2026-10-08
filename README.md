# House Price Prediction
A Machine Learning regression project that predicts house prices based on property-related features.

## 📌 **Overview**
The goal of this project is to build a machine learning model that can predict house prices using different features of a property.

## 🛠️ **Tech Stack**
- Python
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Streamlit

## 🤖 **Machine Learning**
- **Problem :** Regression
- **Models Evalauted :**
    - Linear Regression
    - Random Forest Regressor
- Data Preprocessing
- Feature Selection
- Model Training
- Model Evaluation

## 🔍 **What I Did**
- Explored and preprocessed the house price dataset
- Selected relevant features for prediction
- Split the dataset into training and testing sets
- Trained Linear Regression and Random Forest Regressor models
- Compared the performance of both models
- Selected Random Forest Regressor as the final model because it performed better
- Integrated the final model into a Streamlit web application

## 🚀 **Live Demo**
👉 **[Try the House Price Prediction App](https://housepriceprediction-pruacdvlozyz3lb5xoyutx.streamlit.app/)**

## 📊 **Results**
The performance of Linear Regression and Random Forest Regressor was compared using training and testing scores.
| Model | Training R2 Score | Testing R2 Score |
| --- | ---: | ---: |
|Linear Regression | 86% | 85% |
|Random Forest Regressor | 91% | 86% |

**Final Model :** Random Forest Regressor

Random Forest regressor achieved a higher testing R2 score than Linear Regression and was selected as the final model for the Streamlit application.

## 💻 **How to Run**
pip install -r requirements.txt

streamlit run app.py

## ⚠️ **Disclaimer**
This project is created **for educational purposes.** The predicted prices are estimates and should not be considered professional real-estate valuations.
