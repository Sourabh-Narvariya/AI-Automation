from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

texts = ["I love this!", "That was awful."]
results = sentiment_analyzer(texts)
for text, res in zip(texts, results):
    print(text, "→", res)