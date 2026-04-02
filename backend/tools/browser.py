import asyncio
from playwright.async_api import async_playwright
import logging

logger = logging.getLogger(__name__)

async def fetch_page_content(url: str, timeout_ms: int = 15000) -> str:
    """Fetches the HTML content of a page using Playwright."""
    html_content = ""
    try:
        async with async_playwright() as p:
            # Running in headless mode for production readiness
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            # Navigate and wait for some network idle or timeout
            logger.info(f"Navigating to {url}")
            await page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            
            # Wait a few extra seconds for dynamic elements
            await page.wait_for_timeout(2000)
            
            html_content = await page.content()
            await browser.close()
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {str(e)}")
    
    return html_content
