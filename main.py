import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained pipeline
with open('model_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.title('Sales Prediction App')

# Input fields
st.sidebar.header('Input Features')

def get_input_features():
    mağaza = st.sidebar.number_input('Store ID', min_value=1, max_value=272)
    məhsul_nomresi = st.sidebar.number_input('Product ID', min_value=1, max_value=110)
    məhsul_sayi = st.sidebar.number_input('Product Quantity', min_value=1, max_value=5)
    qram = st.sidebar.number_input('Gram', min_value=0)
    category = st.sidebar.selectbox('Category', options=['Chicken', 'Salt & Vinegar', 'Other', 'Original', 'Cheese Supreme',
       'Hot & Spicy', 'Nacho Cheese', 'Barbecue'])
    cleaned_mehsul_adi = st.sidebar.selectbox('Cleaned Product Name', options=['S m i t h s', 'T h i n s', 'D o r i t o s', 'C o b s',
       'F r e n c h', 'W W'])
    year = st.sidebar.number_input('Year', min_value=1900, max_value=2100)
    month = st.sidebar.number_input('Month', min_value=1, max_value=12)
    day = st.sidebar.number_input('Day', min_value=1, max_value=31)

    # Create DataFrame from input features
    data = {
        'mağaza': [mağaza],
        'məhsul_nomresi': [məhsul_nomresi],
        'məhsul sayi': [məhsul_sayi],
        'qram': [qram],
        'category': [category],
        'cleaned_mehsul_adi': [cleaned_mehsul_adi],
        'year': [year],
        'month': [month],
        'day': [day]
    }
    input_df = pd.DataFrame(data)

    return input_df

input_features = get_input_features()

# Predict button
if st.button('Predict'):
    try:
        # Make prediction
        prediction = pipeline.predict(input_features)
        st.write(f'Predicted Sales: {prediction[0]:.2f}')
    except KeyError as e:
        st.error(f'KeyError: The input category or product name does not match the trained model. Please check the options.')
    except Exception as e:
        st.error(f'Error: {str(e)}')
