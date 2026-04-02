from typing import List, Tuple
from models.schemas import Product

def analyze_products(products: List[Product]) -> Tuple[Product, List[Product]]:
    """Analyzes products to find the best deal, cheapest, and highest rated."""
    if not products:
        return None, []
        
    valid_prices = [p for p in products if p.price > 0]
    if not valid_prices:
        # Default to first if prices are totally missing
        best = products[0]
        best.is_best = True
        return best, products

    # Find cheapest
    cheapest = min(valid_prices, key=lambda x: x.price)
    cheapest.is_cheapest = True
    
    # Find top rated
    top_rated = max(valid_prices, key=lambda x: x.rating)
    top_rated.is_top_rated = True
    
    # Best deal logic: a mix of good rating and low price. 
    # For simplicity, we choose top_rated as best deal if rating > 4.0, else cheapest.
    best_deal = max(valid_prices, key=lambda x: (x.rating * 1000) / (x.price if x.price > 0 else 1))
    best_deal.is_best = True
    
    return best_deal, products
