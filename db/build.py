import sqlite3
import os

CREATE_USER_DB = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        occupation TEXT NOT NULL,
        area TEXT
    )
    """

USERS_EXAMPLES = [('Marcus Goncalves', 'pass123', 'admin', 'ML engineering'),
                  ('Igo Pereira', 'pass1234', 'admin', 'Data Science')]

INSERT_USERS = """
    INSERT INTO users 
    (name, password, occupation, area) 
    VALUES (?, ?, ?, ?)
"""

def create_db():
    try:
        os.remove('db/example.db')
    except:
        pass
    
    conn = sqlite3.connect('db/example.db')
    cur = conn.cursor()

    cur.execute(CREATE_USER_DB)
    cur.executemany(INSERT_USERS, USERS_EXAMPLES)
    conn.commit()
    conn.close()