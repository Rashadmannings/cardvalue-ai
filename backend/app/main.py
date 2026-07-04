from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router

app = FastAPI(
    title="CardValue AI API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "CardValue AI backend is running"}

@app.get("/cards/search")
def search_cards(query: str):
    return {
        "query": query,
        "results": [
            {
                "id": 1,
                "player": "Victor Wembanyama",
                "year": 2023,
                "brand": "Panini Prizm",
                "card_number": "136",
                "grade": "PSA 10",
                "estimated_value": 1645
            }
        ]
    }