# !pip install -q transformers datasets

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import numpy as np
from sklearn.metrics import accuracy_score, f1_score


imdb = load_dataset("imdb")

# Take a very small subset for quick demo
small_train = imdb["train"].shuffle(seed=42).select(range(100))
small_test  = imdb["test"].shuffle(seed=42).select(range(50))

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_fn(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )

tokenized_train = small_train.map(tokenize_fn, batched=True)
tokenized_test  = small_test.map(tokenize_fn, batched=True)

# Tell Trainer which columns are inputs/labels
tokenized_train = tokenized_train.remove_columns(["text"])
tokenized_test  = tokenized_test.remove_columns(["text"])
tokenized_train.set_format("torch")
tokenized_test.set_format("torch")

num_labels = 2
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=num_labels
)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="weighted")
    }

training_args = TrainingArguments(
    output_dir="./imdb-small-distilbert",
    eval_strategy="epoch", # Changed from evaluation_strategy
    logging_strategy="steps",
    logging_steps=10,
    save_strategy="epoch",
    num_train_epochs=2,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,
    weight_decay=0.01,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_test,
    compute_metrics=compute_metrics,

)

trainer.train()

eval_results = trainer.evaluate()
print("Eval results:", eval_results)

# Test on custom sentences
test_texts = ["This movie was fantastic!", "Worst film I have ever seen."]
enc = tokenizer(test_texts, return_tensors="pt", padding=True, truncation=True)
outputs = model(**enc)
preds = outputs.logits.argmax(dim=-1).tolist()
for text, p in zip(test_texts, preds):
    print(text, "->", "positive" if p == 1 else "negative")