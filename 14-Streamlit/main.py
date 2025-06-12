import streamlit as st
import pandas as pd
import numpy as np

st.title("First streamlit application")

name = st.text_input("Enter your name")

age = st.slider("Select you age", 0, 100, 18)

subject_options = ['Python', 'C', 'JavaScript', 'Java', 'Rust']

fav_subject = st.selectbox("Choose your favorite programming language", subject_options)

if name:
    st.write(f"Name: {name}")

st.write(f"Age: {age}")

if fav_subject:
    st.write(f"Favorite programming language: ", fav_subject)

df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write(df)

st.line_chart(df)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=None)
    st.write(df)


st.button("Choose this")

