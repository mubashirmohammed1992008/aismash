from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    title: str
    site: str           # "amazon" | "flipkart"
    price: float
    currency: str       # "INR" | "USD"
    rating: float       # 0.0 - 5.0
    review_count: int
    url: str
    image_url: Optional[str] = None
    original_price: Optional[float] = None
    discount_percentage: Optional[int] = None
    offers: Optional[List[str]] = None
    is_best: bool = False
    is_cheapest: bool = False
    is_top_rated: bool = False

class ReviewSummary(BaseModel):
    pros: List[str]     # 3-5 bullet points
    cons: List[str]     # 3-5 bullet points
    verdict: str        # 2-3 sentence AI recommendation

class SearchResponse(BaseModel):
    query: str
    best_product: Product
    all_results: List[Product]
    review_summary: ReviewSummary
    total_found: int
    scrape_time_seconds: float
