import httpx
import json
import asyncio

SERP_API_KEY = "43ce8d7e296a9d0575c41a7593294faa31a5ba2a43ebc32841176c4a542289e3"

async def test_amazon():
    print("Testing Amazon Engine...")
    url = f"https://serpapi.com/search.json?engine=amazon&amazon_domain=amazon.in&term=iphone+15&api_key={SERP_API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    data = resp.json()
    results = data.get("amazon_results", [])
    if results:
        for i, item in enumerate(results[:3]):
            print(f"[{i}] Title:", item.get("title"))
            print(f"[{i}] Price dict/val:", item.get("price", "NO PRICE"))
            print(f"[{i}] Link:", item.get("link", "NO LINK"))
    else:
        print("No amazon_results!")

async def test_flipkart():
    print("\nTesting Organic Search for true URL...")
    title = "Used Apple iPhone 13 5G 128GB Midnight"
    domain = "buy.budli.in"
    url = f"https://serpapi.com/search.json?engine=google&q={urllib.parse.quote(title + ' site:' + domain)}&num=1&api_key={SERP_API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    data = resp.json()
    org_results = data.get("organic_results", [])
    if org_results:
        link = org_results[0].get("link")
        print(f"EXACT TRUE LINK FOUND: {link}")
    else:
        print("No organic results!")

async def main():
    await test_amazon()
    await test_flipkart()

if __name__ == "__main__":
    asyncio.run(main())
