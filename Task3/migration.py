
import mysql.connector
from pymongo import MongoClient

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
mycursor = mydb.cursor()

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["yourdatabase"]
collection = mongo_db["yourcollection"]

# Retrieve data from MySQL
mycursor.execute("SELECT * FROM yourtable")
result = mycursor.fetchall()

# Migrate data to MongoDB
for row in result:
  data = {
    "column1": row[0],
    "column2": row[1],
    "column3": row[2],
    # Map each column from MySQL to the corresponding field in MongoDB
  }
  collection.insert_one(data)

# Close connections
mycursor.close()
mydb.close()
client.close()
