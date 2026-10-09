import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium Prediction")
st.markdown("Enter the details Below")

#InputFields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight (in  KG)", min_value= 1.0, value=65.0)
height = st.number_input("Height (in  meters)", min_value= 0.5, max_value=2.5, value=1.70)
income_lpa = st.number_input("Annual Income in LPA", min_value=1.0, value=10.0)
smoker = st.selectbox("Are u smoker?",options=['True', 'False'])
city = st.text_input("City",value = 'Mumbai')
occupation = st.selectbox("occupation", ['retired', 'freelancer', 'student', 'government_job', 'business_owner',
                                  'unemployed', 'private_job'])

if st.button("predict premium category"):
    input_data = {
        "age" : age, 
        "weight" : weight,
        "height" : height,
        "income_lpa" : income_lpa,
        "smoker" : smoker,
        "city" : city,
        "occupation" : occupation        
    }
    
    try:
        response = requests.post(API_URL, json = input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(
    f"Predicted premium category: **{result['predicted_category']}**"
)
            st.write("API Response:", result)
            
        else:
            st.error(f"API_Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. make sue it's running on port 8000")
        
