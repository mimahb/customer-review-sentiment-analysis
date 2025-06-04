import pandas as pd
import numpy as np
from transformers import pipeline
from tqdm import tqdm
import pickle

#load and preprocess dataset
df = pd.read_csv('Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv')

sentiment_analyser = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Drop rows with missing reviews
df = df.dropna(subset=["reviews.text"])

# Run prediction on first 5 reviews
sample_reviews = df["reviews.text"].head(20).tolist()
results = sentiment_analyser(sample_reviews)

# Combine results
for review, result in zip(sample_reviews, results):
    print(f"Review: {review[:60]}...")
    print(f"→ Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")