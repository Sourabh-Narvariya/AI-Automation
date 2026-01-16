import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import gradio as gr
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

def generate_text(input):
  input_ids = tokenizer.encode(input, return_tensors="pt")
  with torch.no_grad():
    output = model.generate(
        input_ids,
        max_new_tokens =100,
        do_sample=True,
        temperature = 0.8,
        top_p=0.95,
        repetition_penalty=1.2
      )
  return tokenizer.decode(output[0], skip_special_tokens=True)


gr.Interface(fn=generate_text,
             inputs="textbox", outputs=gr.Textbox(lines=50), title="Text Generation Using Gradio").launch(share=True)
