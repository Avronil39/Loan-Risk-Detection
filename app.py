import pandas as pd
import streamlit as st
import pickle

# Load your model (update path if needed)
with open('model_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)


st.set_page_config(page_title="Loan Prediction", page_icon="💰")

st.title("💼 Loan Risk Detection App")
st.write("Fill the form below to predict the loan risk based on customer details.")

with st.form("loan_form"):
    st.header("Customer Details")

    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Age', min_value=18, max_value=60, step=1)
        sex = st.selectbox('Sex', ['male', 'female'])
        job = st.selectbox('Job', [0, 1, 2, 3])
        housing = st.selectbox('Housing', ['own', 'free', 'rent'])
    
    with col2:
        saving_accounts = st.selectbox('Saving Accounts', ['little', 'moderate','quite rich', 'rich'])
        checking_account = st.selectbox('Checking Account', ['little', 'moderate', 'rich'])
        credit_amount = st.number_input('Credit Amount', min_value=100, step=1)  # Minimum 100
        duration = st.number_input('Duration (in months)', min_value=3, max_value=120, step=1)  # Minimum 3 months
        purpose = st.selectbox('Purpose', [
            'radio/TV', 'education', 'furniture/equipment', 'car', 'business',
            'domestic appliances', 'repairs', 'vacation/others'
        ])

    submitted = st.form_submit_button("Predict Loan Risk 🚀")

# Check if the conditions are met
if submitted:
    if credit_amount < 100:
        st.error("❌ Credit amount should be at least 100.")
    elif duration < 3:
        st.error("❌ Duration should be at least 3 months.")
    else:
        repayment_age = age + duration // 12
        user_input = [
            job,
            housing,
            saving_accounts,
            checking_account,
            credit_amount,
            purpose,
            repayment_age
        ]
        
        dataFrameCols = ['Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Purpose', 'Repayment Age']
        df = pd.DataFrame([user_input], columns=dataFrameCols)
        
        # Make a prediction using the model
        prediction = model.predict(df)
        
        if prediction == 0:
            st.success("NO RISK")
        else:
            st.error("RISKY")
      