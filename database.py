import sqlite3
from datetime import datetime

DATABASE = "database/scraper.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_tables():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        author TEXT,
        tags TEXT,
        scraped_at TEXT

    )
    """)

    conn.commit()
    conn.close()


from datetime import datetime

def insert_quote(quote, author, tags):

    conn = connect()
    cursor = conn.cursor()

    # Check if quote already exists
    cursor.execute(
        "SELECT id FROM quotes WHERE quote = ?",
        (quote,)
    )

    existing = cursor.fetchone()

    if existing:
        print("Duplicate found. Skipping...")
    else:
        cursor.execute("""
        INSERT INTO quotes
        (quote, author, tags, scraped_at)
        VALUES (?, ?, ?, ?)
        """, (
            quote,
            author,
            tags,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()

    conn.close()


def get_all_quotes():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM quotes
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_all():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quotes")

    conn.commit()
    conn.close()


def count_quotes():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM quotes
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def unique_authors():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(DISTINCT author)
    FROM quotes
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


create_tables()