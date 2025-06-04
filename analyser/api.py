from ninja import Router
from pydantic import BaseModel
from typing import List
from .utils import analyze_texts

router = Router()

class ReviewRequest(BaseModel):
    reviews: List[str]

@router.post("/analyze")
def analyze_sentiment(request, data: ReviewRequest):
    results = analyze_texts(data.reviews)
    return {"results": results}
