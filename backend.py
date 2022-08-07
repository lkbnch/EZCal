import sqlite3

# connect to database
conn = None
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

rows = cursor.execute("SELECT id, title, complete FROM todo").fetchall()
print(rows)







def split_event():
    # split event into work blocks + 5 min breaks
    pass

conn.close()