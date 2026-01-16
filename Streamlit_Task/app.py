import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Hello AI", page_icon="🤖")
st.title("Hello AI")
st.write("A tiny demo where a simple local 'AI' responds to your message.")

if "name" not in st.session_state:
	st.session_state["name"] = ""
if "prompt" not in st.session_state:
	st.session_state["prompt"] = ""
if "response" not in st.session_state:
	st.session_state["response"] = None
if "last_time" not in st.session_state:
	st.session_state["last_time"] = None

with st.form("hello_form"):
	st.text_input("Your name", key="name")
	st.text_area("Say something to the AI", key="prompt", height=120)
	submitted = st.form_submit_button("Send")
	if submitted:
		msg = st.session_state["prompt"].strip()
		if not msg:
			st.warning("Please enter a message.")
		else:
			templates = [
				"Hello {name}! I hear you: \"{msg}\"",
				"Hi {name}, here's a quick thought on that: \"{msg}\"",
				"{name}, thanks — you wrote: \"{msg}\"",
				"Got it, {name}. Short summary: \"{msg}\""
			]
			resp = random.choice(templates).format(name=st.session_state["name"] or "friend", msg=msg)
			resp += "\n\n" + f"Quick analysis: {len(msg.split())} words, {len(msg)} chars."
			st.session_state["response"] = resp
			st.session_state["last_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

col1, col2 = st.columns([1, 1])
with col1:
	if st.button("Clear"):
		st.session_state["name"] = ""
		st.session_state["prompt"] = ""
		st.session_state["response"] = None

with col2:
	if st.session_state["prompt"]:
		st.download_button("Download message", data=st.session_state["prompt"], file_name="message.txt")

if st.session_state["response"]:
	st.markdown("### AI Response")
	st.write(st.session_state["response"])
	st.caption(f"Generated at {st.session_state['last_time']}")
