from data.documents import documents
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database.db import get_click_count


doc_texts = [
    doc["title"] + " " + doc["content"]
    for doc in documents
]

vectorizer = TfidfVectorizer(stop_words="english")

document_vectors = vectorizer.fit_transform(doc_texts)


def search(query):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    ranked_results = []

    for index, score in enumerate(similarities):

        if score > 0:

            doc = documents[index]

            click_count = get_click_count(
                query,
                doc["title"]
            )

            boosted_score = score + (
                click_count * 0.1
            )
            print(f"Original Score: {score}")
            print(f"Clicks: {click_count}")
            print(f"Boosted Score: {boosted_score}")

            ranked_results.append(
                (boosted_score, doc)
            )

    ranked_results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked_results