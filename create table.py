from mysql import connector

# Connect to the database
import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    host='localhost',
    database='customers'
)
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)
# mycursor.execute("CREATE TABLE users (name VARCHAR(255), age VARCHAR(255), city VARCHAR(255))")
sql = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
val = [
  ('Peter', '15', 'London'),
  ('Amy', '20', 'Deli'),
  ('Hannah', '36', 'Montevideo'),
  ('Michael', '21', 'Valle'),
  ('Sandy', '25', 'Vegas'),
  ('Betty', '21', 'Chester'),
  ('Richard', '54', 'Washington'),
  ('Susan', '22', 'Yerevan'),
  ('Vicky', '58', 'Sevan'),
  ('Ben', '29', 'Paris'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")