# Customer Churn Prediction  

## Project Overview  
This project focuses on predicting **customer churn**, a key metric for industries such as banking and telecommunications. Churn prediction helps businesses identify customers likely to leave, enabling them to take proactive measures.  

We experimented with various machine learning models, including:  
- **Logistic Regression**  
- **Random Forest Classifier**  
- **XGBoost**

Among these, **XGBoost** delivered the best performance in terms of accuracy and overall metrics.  

---

## Dataset Description  

### Files  
- **train.csv** - The training dataset; `Exited` is the binary target variable.  
- **test.csv** - The test dataset; your objective is to predict the probability of `Exited`.  
- **sample_submission.csv** - A sample submission file in the correct format.  

You can access the dataset and files [here](https://www.kaggle.com/competitions/playground-series-s4e1/data).  

The dataset includes customer attributes such as:  
- Demographics  
- Account information  
- Communication history  
- Service usage  

The target variable indicates whether a customer has churned (left the company) or not.  

---

## Key Steps in the Project  

1. **Data Preprocessing**  
   - Cleaning the dataset by handling missing values and inconsistencies.  
   - Encoding categorical features to make the data suitable for machine learning.  

2. **Exploratory Data Analysis (EDA)**  
   - Analyzing patterns and trends to gain insights into customer behavior.  

3. **Model Building and Evaluation**  
   - Experimenting with machine learning models: Logistic Regression, Random Forest Classifier, and XGBoost.  
   - XGBoost outperformed other models in terms of accuracy and overall metrics.  

4. **Feature Importance Analysis**  
   - Identifying key features that significantly influence customer churn.  

5. **Prediction**  
   - Using the test dataset to predict customer churn and validate the model's performance.  

---

## Tools and Libraries Used  

- **Python**: Scripting and implementation.  
- **Pandas**: Data manipulation.  
- **Matplotlib** and **Seaborn**: Data visualization.  
- **Scikit-learn**: Model building and evaluation.  
- **XGBoost**: Best-performing machine learning model.  




4. **Run the Notebook**

 - Preprocess the data.
 - Train the models.
 - Make predictions.
