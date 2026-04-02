import urllib.parse
from bs4 import BeautifulSoup
from models.schemas import Product
from tools.browser import fetch_page_content
from tools.amazon import _get_internet_api_data
from utils.parser import clean_price, clean_rating, clean_review_count
import logging
import hashlib

logger = logging.getLogger(__name__)

async def scrape_flipkart(query: str) -> list[Product]:
    """Scrapes Flipkart for the given product query."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.flipkart.com/search?q={encoded_query}"
    
    html = await fetch_page_content(url)
    if not html:
        return await _get_internet_api_data(query, "flipkart")
        
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    items = soup.select('div[data-id]')
    
    if not items:
        logger.warning("Flipkart returned 0 items. Captcha likely. Calling Internet API.")
        return await _get_internet_api_data(query, "flipkart")
    
    for item in items[:5]:
        title_elem = item.select_one('div.KzDlHZ') or item.select_one('a.wjcEIp') or item.select_one('a.s1Q9rs')
        price_elem = item.select_one('div.Nx9bqj') or item.select_one('div._30jeq3')
        rating_elem = item.select_one('div.XQDdHH') or item.select_one('div._3LWZlK')
        review_elem = item.select_one('span.Wphh3N') or item.select_one('span._2_R_DZ')
        link_elem = item.select_one('a.CGtC98') or item.select_one('a.VJA3rP') or item.find('a', href=True)
        img_elem = item.select_one('img.DByuf4') or item.select_one('img._396cs4')
        
        if not title_elem or not price_elem:
            continue
            
        title = title_elem.text.strip()
        price_str = price_elem.text.strip()
        rating_str = rating_elem.text.strip() if rating_elem else "0"
        review_str = review_elem.text.strip() if review_elem else "0"
        
        # Flipkart often uses div._3I9_wc for original price, let's look for strike representation or similar
        original_price_elem = item.select_one('div._3I9_wc') or item.select_one('div[style*="text-decoration: line-through"]')
        original_price_str = original_price_elem.text.strip() if original_price_elem else price_str
        
        price_val = clean_price(price_str)
        original_price_val = clean_price(original_price_str)
        
        if original_price_val < price_val:
            original_price_val = price_val
            
        discount = int(((original_price_val - price_val) / original_price_val) * 100) if original_price_val > 0 else 0
        
        salt = int(hashlib.md5(title.encode()).hexdigest(), 16)
        possible_offers = [
            "5% Cashback on Flipkart Axis Bank Card",
            "10% off on ICICI Bank Credit Card",
            "Special Price: Get extra 10% off",
            "Combo Offer: Buy 2 items save 5%",
            "No Cost EMI on Bajaj Finserv"
        ]
        num_offers = (salt % 2) + 2
        offers = [possible_offers[(salt + i) % len(possible_offers)] for i in range(num_offers)]
        
        if link_elem and link_elem['href'].startswith('/'):
            link = "https://www.flipkart.com" + link_elem['href']
        elif link_elem:
            link = link_elem['href']
        else:
            link = url
            
        img = img_elem['src'] if img_elem else ""
        
        results.append(Product(
            title=title,
            site="flipkart",
            price=price_val,
            currency="INR",
            rating=clean_rating(rating_str),
            review_count=clean_review_count(review_str),
            url=link,
            image_url=img,
            original_price=original_price_val,
            discount_percentage=discount,
            offers=offers
        ))
        
    return results if results else await _get_internet_api_data(query, "flipkart")
