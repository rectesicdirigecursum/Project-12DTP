# a python programme to input data into the debate motions database
# 22343 - Thu 1 May

import sqlite3

SQLNAME = "database.db"

def execute_query(query, database=SQLNAME):
    conn = sqlite3.connect(SQLNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
