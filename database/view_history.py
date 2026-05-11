import sqlite3


connection = sqlite3.connect("search_engine.db")
cursor = connection.cursor()


print("\nSEARCH HISTORY:\n")

cursor.execute(
    "SELECT * FROM search_history"
)

for row in cursor.fetchall():
    print(row)


print("\nCLICKS:\n")

cursor.execute(
    "SELECT * FROM clicks"
)

for row in cursor.fetchall():
    print(row)