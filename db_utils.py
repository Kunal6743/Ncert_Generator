import sqlite3
import os

# ===== SAME DB FILE EVERYWHERE =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "ncert_syllabus.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


# ------------------ GET CHAPTER LIST ------------------
def get_chapters(class_no, subject):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT chapter_id, chapter_no, chapter_name
        FROM chapters
        WHERE "class" = ? AND subject = ?
        ORDER BY chapter_no
    """, (class_no, subject))

    rows = cur.fetchall()
    conn.close()
    return rows


# ------------------ GET CHAPTER CONTENT ------------------
def get_chapter_context(chapter_id):
    """
    Returns (chapter_name, key_topics) for AI prompt
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT chapter_name, key_topics
        FROM chapters
        WHERE chapter_id = ?
    """, (chapter_id,))

    row = cur.fetchone()
    conn.close()

    if row:
        return row[0], row[1]
    else:
        return None, None
