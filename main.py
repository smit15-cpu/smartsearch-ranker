from search.engine import search
from database.db import save_search, save_click


query = input("Search: ")

results = search(query)

print("\nResults:\n")

for index, (score, doc) in enumerate(results, start=1):

    print(f"{index}. {doc['title']}")
    print(f"Final Score: {score}")
    print(f"Content: {doc['content']}")
    print("-" * 40)

    save_search(
        query,
        doc["title"],
        score
    )



choice = input(
    "\nSelect a result number to simulate click: "
)

if choice.isdigit():

    choice = int(choice)

    if 1 <= choice <= len(results):

        clicked_doc = results[choice - 1][1]

        save_click(
            query,
            clicked_doc["title"]
        )

        print(
            f"\nYou clicked: {clicked_doc['title']}"
        )

    else:
        print("Invalid selection.")
else:
    print("Please enter a valid number.")