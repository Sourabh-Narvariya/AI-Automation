import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from gtts import gTTS

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)
topic = input("Enter blog topic: ")

prompt = f"""
Write a short, clear and informative blog (120-150 words)
on the topic: {topic}.
"""

blog = llm.invoke(prompt).content

print("\n Generated Blog:\n")
print(blog)
tts = gTTS(text=blog, lang="en")

audio_file = "blog_audio1.mp3"
tts.save(audio_file)

print(f"\n Blog converted to speech succe!")
print(f" Audio saved as: {audio_file}")
