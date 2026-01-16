
import streamlit as st
from transformers import pipeline

st.title(" Hugging Face Chat App")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


user_input = st.text_area("Enter your prompt:", height=120)


if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating response..."):
            response = generator(
                user_input,
                max_length=120,
                num_return_sequences=1
            )[0]["generated_text"]

        st.session_state.chat_history.append(
            {
                "user": user_input,
                "bot": response
            }
        )


st.subheader("🗨️ Chat History")

for chat in st.session_state.chat_history:
    st.markdown(f"** You:** {chat['user']}")
    st.markdown(f"** AI:** {chat['bot']}")
    st.markdown("---")
