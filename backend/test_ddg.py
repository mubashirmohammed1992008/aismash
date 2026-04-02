import httpx
import asyncio
import urllib.parse
import re

async def find_exact_url(title, domain):
    try:
        query = urllib.parse.quote(f"{title} site:{domain}")
        url = f"https://html.duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers)
        
        # Look for the actual DuckDuckGo redirect link that leads to the domain
        match = re.search(rf'href="//duckduckgo\.com/l/\?uddg=([^"&]+)', resp.text)
        if match:
            extracted = urllib.parse.unquote(match.group(1))
            if domain in extracted:
                return extracted
        return f"https://{domain} (FALLBACK)"
    except Exception as e:
        return f"Error: {e}"

async def main():
    print(await find_exact_url("Used Apple iPhone 13 5G 128GB Midnight", "buy.budli.in"))

if __name__ == "__main__":
    asyncio.run(main())
