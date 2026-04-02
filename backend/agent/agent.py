import time
from models.schemas import SearchResponse, Product, ReviewSummary
from agent.planner import plan_scraping
from agent.executor import execute_scrapers
from agent.comparator import analyze_products
from agent.reviewer import generate_review
import logging

logger = logging.getLogger(__name__)

async def run(query: str) -> SearchResponse:
    """Main execution flow for Smash AI agent."""
    start_time = time.time()
    
    # 1. Planner decides which sites to target
    sites = await plan_scraping(query)
    logger.info(f"Planned sites: {sites}")
    
    # 2. Executor hits those sites concurrently
    # Note: Using asyncio parallel fetching
    products = await execute_scrapers(sites, query)
    
    # 3. Comparator finds the best deal
    best_deal, all_products_processed = analyze_products(products)
    
    # 4. Reviewer synthesizes pros/cons
    review_summary = await generate_review(best_deal, all_products_processed)
    
    # Ensure there's a fallback product if everything failed to avoid crash
    if not best_deal:
        best_deal = Product(
            title="Fallback Product",
            site="unknown",
            price=0.0,
            currency="INR",
            rating=0.0,
            review_count=0,
            url="https://example.com"
        )
        
    duration = time.time() - start_time
    
    return SearchResponse(
        query=query,
        best_product=best_deal,
        all_results=all_products_processed,
        review_summary=review_summary,
        total_found=len(all_products_processed),
        scrape_time_seconds=round(duration, 2)
    )
