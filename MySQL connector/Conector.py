import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="Edo",
    passwd="1234",
    database="databaseproject"
)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Jeff", 26))
#db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)