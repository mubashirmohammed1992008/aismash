import json
from llm.client import client
from llm.prompts import SYSTEM_PLANNER_PROMPT
import logging

logger = logging.getLogger(__name__)

async def plan_scraping(query: str) -> list[str]:
    """Uses LLM to decide which sites to scrape. Default to global."""
    try:
        response = await client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=256,
            system=SYSTEM_PLANNER_PROMPT + "\n\nYou should almost always recommend 'global' to search the entire web for the best deals.",
            messages=[
                {"role": "user", "content": f"Query: {query}"}
            ]
        )
        content = response.content[0].text
        data = json.loads(content)
        if isinstance(data, list):
            return data
        if "sites" in data:
            return data["sites"]
        return ["global"]
    except Exception as e:
        logger.warning(f"Planner failed: {str(e)}. Defaulting to global.")
        return ["global"]