import streamlit as st
import pandas as pd

st.title("CSV File Upload & Summary Statistics")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    st.subheader(" Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())
else:
    st.info("Please upload a CSV file to continue.")
