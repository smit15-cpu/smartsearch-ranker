from fastapi import FastAPI
from search.engine import search
from database.db import save_click

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "SmartSearch Ranker API Running"
    }


@app.get("/search")
def search_api(q: str):

    results = search(q)

    formatted_results = []

    for score, doc in results:

        formatted_results.append({
            "title": doc["title"],
            "content": doc["content"],
            "score": score
        })

    return {
        "query": q,
        "results": formatted_results
    }

@app.post("/click")
def register_click(data: dict):

    query = data["query"]
    title = data["title"]

    save_click(query, title)

    return {
        "message": "Click saved successfully"
    }