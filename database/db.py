import sqlite3

DB_NAME = "search_engine.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def save_search(query, title, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO search_history (query, document_title, score)
    VALUES (?, ?, ?)
    """, (query.lower(), title.lower(), score))

    conn.commit()
    conn.close()


def save_click(query, title):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO clicks (query, document_title)
    VALUES (?, ?)
    """, (query.lower(), title.lower()))

    conn.commit()
    conn.close()


def get_click_count(query, title):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM clicks
    WHERE query = ?
    AND document_title = ?
    """, (query.lower(), title.lower()))

    count = cur.fetchone()[0]

    conn.close()
    return count