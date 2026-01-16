# !pip install datasets -q

from datasets import load_dataset

imdb = load_dataset("imdb")  
for i in range(10):
    sample = imdb["train"][i]
    print(f"--- Sample {i+1} ---")
    print("Label:", sample["label"])  
    print("Text:", sample["text"][:500], "...")  
    print()
