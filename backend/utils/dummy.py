import hashlib
import urllib.parse
from models.schemas import Product

# ──────────────────────────────────────────────────────────────────
# Curated product catalog.  Each category has multiple realistic
# products with real Unsplash images, sensible prices, and proper
# buy-links that redirect to actual Amazon / Flipkart search pages.
# ──────────────────────────────────────────────────────────────────

CATALOG = {
    "bag": [
        {
            "title": "Urban Travel Backpack - Waterproof 40L",
            "price": 1499, "img": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&fit=crop",
        },
        {
            "title": "Classic Leather Messenger Bag - Brown",
            "price": 2199, "img": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400&fit=crop",
        },
        {
            "title": "Canvas Tote Bag - Everyday Carry",
            "price": 899, "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400&fit=crop",
        },
        {
            "title": "Laptop Backpack 15.6\" - Anti-Theft",
            "price": 1799, "img": "https://images.unsplash.com/photo-1622560480605-d67c8f0a1b23?w=400&fit=crop",
        },
    ],
    "shoe": [
        {
            "title": "Nike Air Max Running Shoes - Red",
            "price": 4999, "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&fit=crop",
        },
        {
            "title": "Classic White Sneakers - Minimalist",
            "price": 2499, "img": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400&fit=crop",
        },
        {
            "title": "Running Shoes - Lightweight Mesh",
            "price": 3299, "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&fit=crop",
        },
        {
            "title": "Casual Slip-On Loafers - Navy",
            "price": 1899, "img": "https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=400&fit=crop",
        },
    ],
    "laptop": [
        {
            "title": "MacBook Air M2 - 256GB Space Gray",
            "price": 89990, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&fit=crop",
        },
        {
            "title": "HP Pavilion 15 - i5 12th Gen, 16GB RAM",
            "price": 62990, "img": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&fit=crop",
        },
        {
            "title": "Dell Inspiron 14 - Ryzen 5, 512GB SSD",
            "price": 54990, "img": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400&fit=crop",
        },
        {
            "title": "ASUS VivoBook 15 - i3 11th Gen, 8GB",
            "price": 37990, "img": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=400&fit=crop",
        },
    ],
    "phone": [
        {
            "title": "iPhone 15 (128GB) - Blue",
            "price": 69990, "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400&fit=crop",
        },
        {
            "title": "Samsung Galaxy S24 Ultra - 256GB",
            "price": 129999, "img": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400&fit=crop",
        },
        {
            "title": "Google Pixel 8 - 128GB Obsidian",
            "price": 52999, "img": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400&fit=crop",
        },
        {
            "title": "OnePlus 12 - 12GB/256GB Flowy Emerald",
            "price": 64999, "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&fit=crop",
        },
    ],
    "watch": [
        {
            "title": "Apple Watch Series 9 - GPS 45mm",
            "price": 41900, "img": "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=400&fit=crop",
        },
        {
            "title": "Noise ColorFit Pro 5 - AMOLED Display",
            "price": 3499, "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&fit=crop",
        },
        {
            "title": "Fire-Boltt Phoenix Ultra - 1.45\" Display",
            "price": 1499, "img": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400&fit=crop",
        },
        {
            "title": "Samsung Galaxy Watch 6 Classic - 47mm",
            "price": 26999, "img": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400&fit=crop",
        },
    ],
    "headphone": [
        {
            "title": "Sony WH-1000XM5 - Noise Cancelling",
            "price": 26990, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&fit=crop",
        },
        {
            "title": "boAt Rockerz 450 - Wireless On-Ear",
            "price": 1299, "img": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&fit=crop",
        },
        {
            "title": "JBL Tune 760NC - Active Noise Cancelling",
            "price": 4499, "img": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400&fit=crop",
        },
        {
            "title": "Apple AirPods Pro (2nd Gen) - USB-C",
            "price": 24900, "img": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=400&fit=crop",
        },
    ],
    "tv": [
        {
            "title": "Samsung 55\" Crystal 4K UHD Smart TV",
            "price": 42990, "img": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400&fit=crop",
        },
        {
            "title": "LG 43\" 4K UHD Smart LED TV",
            "price": 29990, "img": "https://images.unsplash.com/photo-1567690187548-f07b1d7bf5a9?w=400&fit=crop",
        },
        {
            "title": "Mi 50\" 4K Ultra HD Android Smart TV",
            "price": 31999, "img": "https://images.unsplash.com/photo-1461151304267-38535e780c79?w=400&fit=crop",
        },
        {
            "title": "Sony Bravia 55\" OLED 4K Google TV",
            "price": 119990, "img": "https://images.unsplash.com/photo-1558888401-3cc1de77652d?w=400&fit=crop",
        },
    ],
    "camera": [
        {
            "title": "Canon EOS R50 - Mirrorless (Body Only)",
            "price": 62990, "img": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400&fit=crop",
        },
        {
            "title": "Sony Alpha 6400 - APS-C Mirrorless",
            "price": 74990, "img": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&fit=crop",
        },
        {
            "title": "GoPro HERO12 Black - Action Camera",
            "price": 39490, "img": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400&fit=crop",
        },
        {
            "title": "Nikon Z30 - Vlogging Camera Kit",
            "price": 59990, "img": "https://images.unsplash.com/photo-1495707902641-75cac588d2e9?w=400&fit=crop",
        },
    ],
}

# Keywords that map to catalog categories
KEYWORD_MAP = {
    "bag": "bag", "backpack": "bag", "purse": "bag", "handbag": "bag",
    "rucksack": "bag", "satchel": "bag", "tote": "bag",
    "shoe": "shoe", "sneaker": "shoe", "sandal": "shoe", "boot": "shoe",
    "slipper": "shoe", "loafer": "shoe", "heel": "shoe",
    "laptop": "laptop", "macbook": "laptop", "notebook": "laptop",
    "chromebook": "laptop",
    "phone": "phone", "iphone": "phone", "samsung": "phone", "pixel": "phone",
    "oneplus": "phone", "smartphone": "phone", "mobile": "phone",
    "redmi": "phone", "realme": "phone", "vivo": "phone", "oppo": "phone",
    "watch": "watch", "smartwatch": "watch",
    "headphone": "headphone", "earphone": "headphone", "earbuds": "headphone",
    "airpods": "headphone", "headset": "headphone",
    "tv": "tv", "television": "tv", "smart tv": "tv",
    "camera": "camera", "dslr": "camera", "mirrorless": "camera",
    "gopro": "camera", "webcam": "camera",
}

# Bank offers pool
BANK_OFFERS = [
    "10% Instant Discount up to ₹1500 on SBI Credit Card",
    "Flat ₹500 off on HDFC Bank Credit Card EMI",
    "5% Unlimited Cashback on Amazon Pay ICICI Card",
    "No Cost EMI starting ₹1,667/month on select cards",
    "Extra ₹1000 off with Flipkart Axis Bank Card",
    "Get ₹100 cashback on Amazon Pay UPI",
    "10% off on ICICI Bank Debit Card Transactions",
    "Flat ₹2000 off on Kotak Bank Credit Card",
]


def _detect_category(query: str) -> str:
    """Find the best matching catalog category for a query."""
    lower = query.lower()
    for keyword, category in KEYWORD_MAP.items():
        if keyword in lower:
            return category
    return ""


def _pick_offers(seed: int, site: str) -> list[str]:
    """Deterministically pick 2-3 bank offers."""
    count = (seed % 2) + 2
    return [BANK_OFFERS[(seed + i) % len(BANK_OFFERS)] for i in range(count)]


def _buy_url(query: str, site: str) -> str:
    """Generate a real search URL that actually works on the target site."""
    q = urllib.parse.quote(query)
    site_lower = site.lower()
    if "amazon" in site_lower:
        return f"https://www.amazon.in/s?k={q}"
    elif "flipkart" in site_lower:
        return f"https://www.flipkart.com/search?q={q}"
    elif "croma" in site_lower:
        return f"https://www.croma.com/searchB?q={q}"
    else:
        return f"https://www.google.com/search?q={q}+buy+online+India"


def get_dummy_products(query: str, site: str) -> list[Product]:
    """
    Generate realistic dummy products for a search query.
    Uses a curated catalog when a category is detected,
    otherwise generates sensible generic results.
    """
    seed = int(hashlib.md5(query.encode()).hexdigest(), 16)
    category = _detect_category(query)

    # Assign sites
    if site.lower() == "global":
        sites = ["Amazon", "Flipkart"]
    else:
        sites = [site.title(), site.title()]

    if category and category in CATALOG:
        items = CATALOG[category]
        # Pick 4 products, rotating through the catalog deterministically
        products = []
        for i in range(min(4, len(items))):
            idx = (seed + i) % len(items)
            item = items[idx]
            chosen_site = sites[i % len(sites)]
            item_seed = seed + i

            original_price = round(item["price"] * 1.25)
            discount = int(((original_price - item["price"]) / original_price) * 100)

            products.append(Product(
                title=item["title"],
                site=chosen_site,
                price=float(item["price"]),
                currency="INR",
                rating=round(4.0 + ((item_seed % 10) / 10.0), 1),
                review_count=(item_seed % 5000) + 200,
                url=_buy_url(item["title"], chosen_site),
                image_url=item["img"],
                original_price=float(original_price),
                discount_percentage=discount,
                offers=_pick_offers(item_seed, chosen_site),
            ))
        return products
    else:
        # Generic fallback for unknown categories
        # Use a neutral product image
        dynamic_price = 1000.0 + (seed % 20000)
        original_price = round(dynamic_price * 1.25)
        discount = int(((original_price - dynamic_price) / original_price) * 100)

        price_2 = round(dynamic_price * 1.15)
        original_price_2 = round(price_2 * 1.25)
        discount_2 = int(((original_price_2 - price_2) / original_price_2) * 100)

        return [
            Product(
                title=f"Premium {query.title()} - Best Seller",
                site=sites[0],
                price=dynamic_price,
                currency="INR",
                rating=round(4.0 + ((seed % 10) / 10.0), 1),
                review_count=(seed % 5000) + 100,
                url=_buy_url(query, sites[0]),
                image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&fit=crop",
                original_price=float(original_price),
                discount_percentage=discount,
                offers=_pick_offers(seed, sites[0]),
            ),
            Product(
                title=f"{query.title()} (Top Rated) - Limited Deal",
                site=sites[1],
                price=float(price_2),
                currency="INR",
                rating=round(min(5.0, 4.0 + ((seed % 10) / 10.0) + 0.2), 1),
                review_count=(seed % 3000) + 500,
                url=_buy_url(query, sites[1]),
                image_url="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400&fit=crop",
                original_price=float(original_price_2),
                discount_percentage=discount_2,
                offers=_pick_offers(seed + 1, sites[1]),
            ),
        ]
