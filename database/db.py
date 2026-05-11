import sqlite3


connection = sqlite3.connect("search_engine.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS search_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    document_title TEXT,
    score REAL
)
""")

connection.commit()


def save_search(query, title, score):
    cursor.execute("""
    INSERT INTO search_history (query, document_title, score)
    VALUES (?, ?, ?)
    """, (query, title, score))

    connection.commit()