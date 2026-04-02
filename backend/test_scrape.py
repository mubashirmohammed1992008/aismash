import asyncio
from tools.amazon import scrape_amazon
from tools.flipkart import scrape_flipkart
from tools.browser import fetch_page_content

async def main():
    print("Testing Amazon...")
    amz = await scrape_amazon("iphone 15")
    print(f"Amazon results: {len(amz)}")
    if not amz:
        html = await fetch_page_content("https://www.amazon.in/s?k=iphone+15")
        print(f"Amazon HTML length: {len(html)}")
        with open("amz_debug.html", "w") as f:
            f.write(html)
            
    print("Testing Flipkart...")
    fk = await scrape_flipkart("iphone 15")
    print(f"Flipkart results: {len(fk)}")
    if not fk:
        html = await fetch_page_content("https://www.flipkart.com/search?q=iphone+15")
        print(f"Flipkart HTML length: {len(html)}")
        with open("fk_debug.html", "w") as f:
            f.write(html)

asyncio.run(main())
