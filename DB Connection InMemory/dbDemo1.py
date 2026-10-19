import sqlite3

#set connection to database
conn = sqlite3.connect("school.db")

#cursor object creation
cur = conn.cursor()

#creating table

cur.execute("""

CREATE TABLE IF NOT EXISTS STUDENT(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
marks REAL)

""")

#comiting the canges
conn.commit()

#inserting values 

# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("ram", 12, 56.67))
# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("sita", 11, 68.67))
# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("shyam", 15, 89.45))
# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("radha", 18, 89.45))
# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("radha", 12, 99.45))
# cur.execute("insert into student(name, age, marks) values(?, ?, ?)", ("radha", 15, 78.85))
# conn.commit()

#fetching data from the table

# cur.execute("select * from student")
# student = cur.fetchall() #fetches all data
# student = cur.fetchone() #fetches the first data
# student = cur.fetchmany(3) #fetches given  amount of rows

# cur.execute("select * from student where name = ?", ("radha", ))
# student = cur.fetchall()
# print(student)

# conn.commit()

#update record

# cur.execute("update student set marks = ? where name = ?", (88.88,"ram"))
# conn.commit()

#deleting record

cur.execute("DELETE from student where name =?",("ram",))
conn.commit()

conn.close()