import sqlite3


connection = sqlite3.connect("search_engine.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM search_history")

rows = cursor.fetchall()

for row in rows:
    print(row)