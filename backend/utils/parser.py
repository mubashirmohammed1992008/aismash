import re
from bs4 import BeautifulSoup

def clean_price(price_str: str) -> float:
    """Extracts a float number from a currency string like '₹ 45,000' or '$50.99'."""
    if not price_str:
        return 0.0
    # Remove currency symbols, commas, and spaces
    clean_str = re.sub(r'[^\d.]', '', price_str)
    try:
        return float(clean_str)
    except ValueError:
        return 0.0

def clean_rating(rating_str: str) -> float:
    """Extracts a rating float, e.g. '4.5 out of 5' -> 4.5"""
    if not rating_str:
        return 0.0
    match = re.search(r'([\d.]+)', rating_str)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return 0.0
    return 0.0

def clean_review_count(count_str: str) -> int:
    """Extracts total review count '1,234 reviews' -> 1234"""
    if not count_str:
        return 0
    clean_str = re.sub(r'[^\d]', '', count_str)
    try:
        return int(clean_str)
    except ValueError:
        return 0
