import torch
import numpy as np
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

speaker_embeddings = torch.randn(1, 512)

text = "Hello Sourabh, this text is converted into speech using Hugging Face on Google Colab."

inputs = processor(text=text, return_tensors="pt")

speech_embeddings = model.generate_speech(inputs["input_ids"], speaker_embeddings)

with torch.no_grad():
    speech = vocoder(speech_embeddings)

print("Speech generated successfully!")
print(f"Speech shape: {speech.shape}")

if len(speech.shape) == 2:
    audio_length = speech.shape[1] / 22050
else:
    audio_length = speech.shape[0] / 22050

print(f"Audio length: {audio_length:.2f} seconds")
print(f"Sampling rate: 22050 Hz")

from IPython.display import Audio

audio_np = speech.numpy().squeeze()
if audio_np.max() > 1.0:
    audio_np = audio_np / np.abs(audio_np).max()

print(f"Audio data shape after squeeze: {audio_np.shape}")
print(f"Audio min: {audio_np.min():.4f}, max: {audio_np.max():.4f}")

display(Audio(audio_np, rate=22050))