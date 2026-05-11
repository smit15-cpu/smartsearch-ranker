from search.engine import search
from database.db import save_search


query = input("Search: ")

results = search(query)

print("\nResults:\n")

for score, doc in results:
    print(f"Score: {score}")
    print(f"Title: {doc['title']}")
    print(f"Content: {doc['content']}")
    print("-" * 40)

    save_search(
        query,
        doc["title"],
        score
    )