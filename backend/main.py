import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from models.schemas import SearchResponse
from agent import agent
from utils.url_parser import extract_product_name

app = FastAPI(title="Smash AI Backend", description="Agentic AI Shopping Assistant")

# Allows all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/search", response_model=SearchResponse)
async def search(product: str):
    if not product:
        raise HTTPException(status_code=400, detail="Product query is required")
    
    try:
        # Await the async run method on the orchestrator agent
        result = await agent.run(product)
        return result
    except Exception as e:
        # Graceful fallback logic should be inside agent.run ideally,
        # but if it fails completely we return 500
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze", response_model=SearchResponse)
async def analyze_url(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required")
        
    try:
        # 1. Parse the URL to get the core product name
        product_name = await extract_product_name(url)
        
        if not product_name:
            raise ValueError("Could not extract a valid product name from the URL")
            
        # 2. Run the exact same agent orchestrator using the derived name
        result = await agent.run(product_name)
        
        # 3. We optionally could inject the original URL into the results 
        # or bias the comparator, but for now we just return the global search!
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
