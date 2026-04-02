import json
from llm.client import client
from llm.prompts import SYSTEM_PLANNER_PROMPT
import logging

logger = logging.getLogger(__name__)

async def plan_scraping(query: str) -> list[str]:
    """Uses LLM to decide which sites to scrape. Default to global."""
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PLANNER_PROMPT + "\n\nYou should almost always recommend 'global' to search the entire web for the best deals."},
                {"role": "user", "content": f"Query: {query}"}
            ],
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        data = json.loads(content)
        # Expected e.g. {"sites": ["global"]} fallback below
        if isinstance(data, list):
            return data
        if "sites" in data:
            return data["sites"]
        return ["global"]
    except Exception as e:
        logger.warning(f"Planner failed: {str(e)}. Defaulting to global.")
        return ["global"]
