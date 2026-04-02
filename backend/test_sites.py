import asyncio
from tools.browser import fetch_page_content
from bs4 import BeautifulSoup
import urllib.parse

async def test_ebay():
    query = "iphone 15"
    url = f"https://www.ebay.com/sch/i.html?_nkw={urllib.parse.quote(query)}"
    print(f"Fetching {url}")
    html = await fetch_page_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.s-item')
    print(f"eBay returned {len(items)} items")
    for item in items[1:3]: # skip the first which is usually a "shop on ebay" ad
        title = item.select_one('.s-item__title')
        price = item.select_one('.s-item__price')
        if title and price:
            print("eBay:", title.text, price.text)

async def test_croma():
    query = "iphone 15"
    url = f"https://www.croma.com/searchB?q={urllib.parse.quote(query)}%3Arelevance&text={urllib.parse.quote(query)}"
    print(f"Fetching {url}")
    html = await fetch_page_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.product-item') # generic guess, might be wrong
    print(f"Croma returned {len(items)} items")
    # croma is react/SPA, might require waiting? Our fetch_page_content waits for timeout

async def main():
    await test_ebay()
    await test_croma()

if __name__ == "__main__":
    asyncio.run(main())
