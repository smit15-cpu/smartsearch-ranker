from data.documents import documents
from rank_bm25 import BM25Okapi
from database.db import get_click_count



# PREPARE TOKENS


corpus = [
    (doc["title"] + " " + doc["content"]).lower().split()
    for doc in documents
]

bm25 = BM25Okapi(corpus)



# SEARCH FUNCTION

def search(query):

    query_tokens = query.lower().split()

    scores = bm25.get_scores(
        query_tokens
    )

    ranked_results = []

    for i, score in enumerate(scores):

        doc = documents[i]

        clicks = get_click_count(
            query,
            doc["title"]
        )

        click_boost = (
            clicks * 1.0
        )

        final_score = (
            score +
            click_boost
        )

        explanation = {
            "bm25_score": round(
                float(score),
                3
            ),

            "click_boost": round(
                click_boost,
                3
            ),

            "clicks": clicks,

            "final_score": round(
                final_score,
                3
            )
        }

        ranked_results.append(
            (
                final_score,
                doc,
                explanation
            )
        )

    ranked_results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked_results