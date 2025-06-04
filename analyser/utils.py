from transformers import pipeline

sentiment_analyser = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_texts(reviews):
    return sentiment_analyser(reviews)
