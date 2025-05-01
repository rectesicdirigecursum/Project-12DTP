


import sqlite3

SQLNAME = "database.db"

def execute_query(query, database=SQLNAME):
    conn = sqlite3.connect(SQLNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()