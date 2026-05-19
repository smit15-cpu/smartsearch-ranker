from data.documents import documents
from rank_bm25 import BM25Okapi
from database.db import get_click_count


# -----------------------------
# PREPARE TOKENS
# -----------------------------

corpus = [
    (doc["title"] + " " + doc["content"]).lower().split()
    for doc in documents
]

bm25 = BM25Okapi(corpus)


# -----------------------------
# SEARCH FUNCTION
# -----------------------------

def search(query):

    query_tokens = query.lower().split()

    scores = bm25.get_scores(query_tokens)

    ranked_results = []

    for i, score in enumerate(scores):

        doc = documents[i]

        click_count = get_click_count(
            query,
            doc["title"]
        )

        final_score = score + (click_count * 1.0)

        ranked_results.append(
            (final_score, doc)
        )

    ranked_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return ranked_results