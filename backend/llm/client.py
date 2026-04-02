import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# Provide a dummy string to prevent the app from crashing on import if the key isn't set yet.
# When actual endpoints are hit without a key, the agent's try/except will return fallback data!
client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "dummy-key-to-prevent-import-crash")
)
