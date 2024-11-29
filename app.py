import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title('Customer Bank Churn')

# Input Fields
credit_score = st.number_input('Credit Score', min_value=350, max_value=850)
age = st.number_input('Age', min_value=18, max_value=100)
tenure = st.number_input('Tenure (years)', min_value=0, max_value=10)
balance = st.number_input('Balance', min_value=0.0, step=1000.0, format='%f')
num_of_products = st.selectbox('Number of Products', [1, 2, 3, 4])
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary', min_value=1000.0, step=500.0, format='%f')
geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
gender = st.selectbox('Gender', ['Male', 'Female'])

# Encode categorical features (Geography and Gender)
geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_map = {'Male': 0, 'Female': 1}
geography_encoded = geography_map[geography]
gender_encoded = gender_map[gender]

# Additional Placeholder Features (replace with actual features if known)
additional_feature_1 = 0.0  # Placeholder value
additional_feature_2 = 0.0  # Placeholder value

# Combine all input features into a single array in the specified order
input_features = np.array([[credit_score, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary, geography_encoded, gender_encoded, additional_feature_1, additional_feature_2]])

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_features)
    st.write("## Prediction Result")
    st.write(f"Prediction: {'Yes' if prediction[0] == 1 else 'No'}")
