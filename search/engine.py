from data.documents import documents
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
            ranked_results.append((score, documents[index]))

    ranked_results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked_results