import streamlit as st
import pandas as pd 
from transformers import pipeline

st.title("Streamlit app that uses Hugging Face to generate text from a prompt")
@st.cache_resource
def load_model():
    return pipeline("text-generation", model ="gpt2", temperature=0.7, top_k=50, top_p=0.95)
text_generator = load_model()

prompt = st.text_area("Enter your prompt here", height=150)

if st.button("Generate Text"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        with st.spinner("Generating text..."):
            generated = text_generator(prompt, max_length=80,do_sample=False, num_return_sequences=3, num_beams=3, early_stopping=True)
            st.subheader("Generated Text")
            st.write(generated[0]['generated_text'])