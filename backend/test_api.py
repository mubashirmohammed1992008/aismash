import httpx
r = httpx.get("http://localhost:8000/search", params={"product": "bag"}, timeout=30)
data = r.json()
print(f"Total found: {data['total_found']}")
bp = data["best_product"]
print(f"Best: {bp['title']} | Rs.{bp['price']} | {bp['site']}")
print(f"Image: {bp['image_url']}")
print(f"Buy URL: {bp['url']}")
print(f"---")
for p in data["all_results"]:
    print(f"  {p['title']} | Rs.{p['price']} | {p['site']} | img_ok={bool(p['image_url'])}")
