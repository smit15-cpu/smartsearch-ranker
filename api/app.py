from fastapi import FastAPI
from search.engine import search


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