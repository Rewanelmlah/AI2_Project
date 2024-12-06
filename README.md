# Bank Customer Churn Prediction  

## Project Overview  
This project predicts whether a customer will exit a bank (churn) based on various customer features. The model uses **XGBoost**, a powerful gradient boosting algorithm, to classify whether a customer will leave the bank (`Exited = 1`) or stay (`Exited = 0`).  

---

## Features  
The following features are used to train the model:  

1. **CreditScore**: A score representing the customer's creditworthiness.  
2. **Geography**: The geographical location of the customer (e.g., France, Spain, Germany).  
3. **Gender**: The gender of the customer (Male/Female).  
4. **Age**: The age of the customer.  
5. **Tenure**: The number of years the customer has been with the bank.  
6. **Balance**: The account balance of the customer.  
7. **NumOfProducts**: The number of products the customer has with the bank.  
8. **HasCrCard**: Whether the customer has a credit card (`1` if yes, `0` if no).  
9. **IsActiveMember**: Whether the customer is an active member of the bank (`1` if yes, `0` if no).  
10. **EstimatedSalary**: The estimated salary of the customer.  

---

## Target Label  
The target label is **Exited**, which indicates whether the customer has exited (left) the bank:  

- **Exited = 1**: The customer left the bank.  
- **Exited = 0**: The customer stayed with the bank.  

---

## Model Evaluation and Selection  
In this project, three different machine learning classifiers were evaluated on the bank churn dataset to predict customer churn. The following models were tested:  

1. **Logistic Regression**  
2. **Random Forest Classifier**  
3. **XGBoost Classifier** (final model chosen)  

---

## Steps  

1. **Data Preprocessing**  
   - Cleaned the data by handling missing values and inconsistencies.  
   - Encoded categorical variables (e.g., Geography, Gender) to prepare them for model training.  

2. **Model Training**  
   - Used the **XGBoost Classifier** to train the model with the training data.  

3. **Hyperparameter Tuning**  
   - Tuned hyperparameters of the XGBoost model using **GridSearchCV** to achieve optimal performance.  

4. **Evaluation**  
   - Evaluated the model using metrics such as **AUC**, **F1 score**, and a **classification report** to ensure high accuracy.  

---
## streamlit deployment
