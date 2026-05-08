from data.documents import documents


def search(query):
    query_words = query.lower().split()

    ranked_results = []

    for doc in documents:
        score = 0

        text = (doc["title"] + " " + doc["content"]).lower()

        for word in query_words:
            score += text.count(word)

        if score > 0:
            ranked_results.append((score, doc))

    ranked_results.sort(reverse=True, key=lambda x: x[0])

    return ranked_results