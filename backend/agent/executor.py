import asyncio
from typing import List
from models.schemas import Product
from tools.amazon import scrape_amazon
from tools.flipkart import scrape_flipkart
from tools.global_search import scrape_global
import logging

logger = logging.getLogger(__name__)

async def execute_scrapers(sites: List[str], query: str) -> List[Product]:
    """Runs designated scrapers concurrently using asyncio.gather."""
    tasks = []
    
    # Map site strings to scraper functions
    site_map = {
        "amazon": scrape_amazon,
        "flipkart": scrape_flipkart,
        "global": scrape_global
    }
    
    for site in sites:
        scraper = site_map.get(site.lower())
        if scraper:
            tasks.append(scraper(query))
            
    # Gather results concurrently
    try:
        results = await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        logger.error(f"Execution error: {str(e)}")
        return []

    # Flatten list of lists
    all_products = []
    for res in results:
        if isinstance(res, list):
            all_products.extend(res)
        elif isinstance(res, Exception):
            logger.error(f"Scraper returned exception: {str(res)}")
            
    return all_products
