import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "ncert_syllabus.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check how many chapters per class
cur.execute('SELECT "class", COUNT(*) FROM chapters GROUP BY "class"')
rows = cur.fetchall()

print("📊 Chapters per class:")
for r in rows:
    print(f"Class {r[0]} → {r[1]} chapters")

conn.close()
