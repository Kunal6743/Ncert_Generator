import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "ncert_syllabus.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS chapters (
    chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    "class" INTEGER,
    subject TEXT,
    chapter_no INTEGER,
    chapter_name TEXT,
    key_topics TEXT
)
""")

conn.commit()
conn.close()

print("✅ Table created ONCE")
