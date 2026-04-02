import logging
from bs4 import BeautifulSoup
from tools.browser import fetch_page_content
import re
import urllib.parse

logger = logging.getLogger(__name__)

async def extract_product_name(url: str) -> str:
    """Fetches the supplied URL and extracts the clean product title."""
    try:
        html = await fetch_page_content(url)
        if not html:
            # Try a lightweight fallback before giving up
            raise ValueError("Could not fetch HTML from URL. Anti-bot protection likely active.")
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. Try OG title initially
        og_title = soup.find('meta', property='og:title')
        title_text = og_title['content'] if og_title else ''
        
        # 2. Fallback to <title>
        if not title_text:
            title_tag = soup.find('title')
            title_text = title_tag.text if title_tag else ''
            
        # 3. Aggressive URL parsing fallback
        if not title_text or len(title_text) < 5:
            parsed_url = urllib.parse.urlparse(url)
            path_segments = parsed_url.path.strip('/').split('/')
            
            # Amazon URLs often look like /Apple-iPhone-15-128-GB/dp/B0CHX1W1XY
            # or just /dp/B0CHX1W1XY. If we see a long slug, use it.
            for segment in path_segments:
                if '-' in segment and len(segment) > 10 and not segment.startswith('dp'):
                    title_text = segment.replace('-', ' ')
                    break
                    
            if not title_text and path_segments:
                dirty_slug = path_segments[-1] if 'dp' not in path_segments else path_segments[0]
                title_text = dirty_slug.replace('-', ' ')
                
        if not title_text:
            raise ValueError("Could not determine title from URL structure or contents")

        # 4. Clean up generic site strings
        # E.g. "Apple iPhone 15 (128 GB) - Black : Amazon.in: Electronics"
        
        clean_title = title_text
        
        # Regex to strip common tailing elements
        patterns_to_strip = [
            r' : Amazon\..*',
            r' - Amazon\..*',
            r' \| Flipkart\..*',
            r' \| Buy Online.*',
            r' - Buy Online.*',
            r'Buy .*? Online at Best Price.*',
        ]
        
        for pattern in patterns_to_strip:
            clean_title = re.sub(pattern, '', clean_title, flags=re.IGNORECASE)
            
        # If it looks like "Amazon.in: Buy Apple iPhone 15..."
        if "Amazon" in clean_title and ":" in clean_title:
            parts = clean_title.split(':')
            if len(parts) > 1:
                clean_title = parts[1].replace('Buy', '').strip()

        clean_title = clean_title.strip()
        logger.info(f"Extracted clean title '{clean_title}' from URL")
        return clean_title
        
    except Exception as e:
        logger.error(f"Failed to extract product name from URL {url}: {e}")
        
        # Desperate fallback: regex the URL directly
        match = re.search(r'amazon\.in/([^/]+)/dp', url) or re.search(r'flipkart\.com/([^/]+)/p/', url)
        if match:
            fallback = match.group(1).replace('-', ' ')
            logger.info(f"Used regex fallback to extract: {fallback}")
            return fallback
            
        raise ValueError(f"Could not analyze URL: {str(e)}")
