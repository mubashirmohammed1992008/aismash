import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY", "dummy-key-to-prevent-import-crash")
)