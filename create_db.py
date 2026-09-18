import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(20),
    SECTION VARCHAR(25),
    MARKS INT
)
""")

cursor.execute("INSERT INTO STUDENT VALUES('Kanha', 'DS', 'B', 80)")
cursor.execute("INSERT INTO STUDENT VALUES('Sharon', 'CS', 'A', 89)")
cursor.execute("INSERT INTO STUDENT VALUES('Rohit', 'CSDS', 'C', 60)")
cursor.execute("INSERT INTO STUDENT VALUES('Anna', 'IT', 'D', 87)")

connection.commit()

print("Database created successfully!")

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

connection.close()