import asyncio
from tools.browser import fetch_page_content
from bs4 import BeautifulSoup
import urllib.parse

async def test_smartprix():
    query = "iphone 15"
    url = f"https://www.smartprix.com/products/?q={urllib.parse.quote(query)}"
    print(f"Fetching {url}")
    html = await fetch_page_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.sm-product')
    print(f"Smartprix returned {len(items)} items")

if __name__ == "__main__":
    asyncio.run(test_smartprix())
