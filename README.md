# Customer Review Sentiment Analysis API
This project is a robust sentiment analysis API built with Django and Django Ninja. I used pretrained model from Hugging Face to trained the data on sentiment analysis. It analyzes customer reviews and classifies them as positive, negative, or neutral.

## Features
 Uses a pretrained Hugging Face transformer model for sentiment analysis.

 Provides a REST API endpoint for analyzing review text.

 Easily testable via Postman or any frontend client.

 Built using Django and Django Ninja for fast API development and ready for deployment.

## How to Use
Clone the repo:

git clone https://github.com/mimahb/customer-review-sentiment-analysis.git

Install dependencies:
pip install -r requirements.txt

Run the Django server:
python manage.py runserver

Test the API at:
http://127.0.0.1:8000/api/sentiment/analyze
POST JSON:
{
  "text": "I love this product!"
}

Response:
{
  "label": "POSITIVE",
  "score": 0.9987
}

## Tech Stack
Django

Django Ninja

Hugging Face Transformers

Python 3

