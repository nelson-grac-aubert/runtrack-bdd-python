import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Misstouille83!sql",
    database="LaPlateforme"
)

cursor = database.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

results = cursor.fetchall()
print(results)

cursor.close()

database.close()