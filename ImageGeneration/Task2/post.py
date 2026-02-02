
import pytesseract
from PIL import Image
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

image_path = "image1.png"  
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)

print("Extracted Text ")
print(extracted_text)
clean_text = extracted_text.strip()

prompt = f"""
The following text is extracted from an image using OCR.
Please summarize it in simple words:

{clean_text}
"""

response = llm.invoke(prompt)

print("\nLLM Output ")
print(response.content)