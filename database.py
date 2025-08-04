# database.py

import sqlite3
from datetime import datetime

# Connect to SQLite (or create if it doesn't exist)
def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS query_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call init once (when module is imported)
init_db()

# Function to log each query
def log_query(case_type, case_number, filing_year, result):
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO query_log (case_type, case_number, filing_year, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, str(result), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
