
import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter image prompt: ")

result = client.images.generate(
    model="gpt-image-1",   # DALL·E image model
    prompt=prompt,
    size="1024x1024"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

image = Image.open(io.BytesIO(image_bytes))
image.save("generated_image.png")

print("✅ Image generated and saved as generated_image.png")
