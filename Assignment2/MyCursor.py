import sqlite3

conn = sqlite3.connect('Students.db.sqlite')

class MyCursor:

    def __init__(self):
        myCursor = conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self):
        conn.close()