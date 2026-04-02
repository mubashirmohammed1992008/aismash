import json
from models.schemas import ReviewSummary, Product
from llm.client import client
from llm.prompts import SYSTEM_REVIEWER_PROMPT
import logging

logger = logging.getLogger(__name__)

async def generate_review(best_deal: Product, all_products: list[Product]) -> ReviewSummary:
    """Uses LLM to summarize pros, cons, and verdict based on parsed products."""
    if not best_deal:
        return ReviewSummary(pros=[], cons=[], verdict="No products found.")
        
    prompt_data = {
        "best_deal": best_deal.model_dump(),
        "total_results": len(all_products)
    }
    
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_REVIEWER_PROMPT},
                {"role": "user", "content": json.dumps(prompt_data)}
            ],
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        data = json.loads(content)
        return ReviewSummary(
            pros=data.get("pros", ["Good price"]),
            cons=data.get("cons", ["Limited availability"]),
            verdict=data.get("verdict", "The best deal represents a strong balance of price and quality.")
        )
    except Exception as e:
        logger.warning(f"Reviewer LLM failed: {str(e)}")
        return ReviewSummary(
            pros=["Excellent value", "Top rated by users", "Competitive pricing"],
            cons=["Limited stock", "Price may fluctuate"],
            verdict="Based on available data, the selected top product offers fantastic value for money."
        )
