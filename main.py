import streamlit as st
import pickle 
from sklearn.linear_model import LogisticRegression

vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
category_dict = pickle.load(open('category_dict.pkl', 'rb'))

user = st.input_text(
    "",
    placeholder = "Enter news headline here"
)

# preparing text for vectorization
user = user.replace("\W", " ").lower()

# model = 



