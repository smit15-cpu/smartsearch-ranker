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

cursor.execute("""
CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    document_title TEXT
)
""")

connection.commit()

def save_click(query, title):
    cursor.execute("""
    INSERT INTO clicks (query, document_title)
    VALUES (?, ?)
    """, (query, title))

    connection.commit()

def get_click_count(query, title):

    cursor.execute("""
    SELECT COUNT(*)
    FROM clicks
    WHERE query = ?
    AND document_title = ?
    """, (query, title))

    count = cursor.fetchone()[0]

    return count