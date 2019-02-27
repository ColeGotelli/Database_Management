import sqlite3
from Student import Student

conn = sqlite3.connect('Students.db.sqlite')

stu = Student('Rene', 'foobar', 'idk')

c.execute("INSERT INTO students('First_Name', 'Last_Name', 'major')"
          "VALUES ('Cole', 'Gotelli', 'CS')")

c.execute("INSERT INTO students('First_Name', 'Last_Name', 'major')"
          "VALUES (?, ?, ?), ('rene', 'bar', 'softball')")

conn.commit()
print("record created")

conn.close()