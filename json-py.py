import  os, json
from mysql import connector

# Connect to the database
import mysql.connector


# read JSON file
file = os.path.abspath(r'C:\Users\ASUS\PycharmProjects\pythonProject4\newjson.json')
json_data=open(file).read()
json_obj = json.loads(json_data)

# connect to MySQL
mydb = mysql.connector.connect(
    user='root',
    host='localhost',
    database='customers'
)
mycursor = mydb.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    name =  (item.get("name", None))
    age = (item.get("age", None))
    city = (item.get("city", None))

    mycursor.execute("INSERT INTO users (name,	age, city) VALUES (%s,	%s,	%s)", (name,	age, city))
mydb.commit()
mydb.close()