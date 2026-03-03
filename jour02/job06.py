import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Misstouille83!sql",
    database="LaPlateforme"
)

cursor = database.cursor()

cursor.execute("SELECT capacite FROM salle")

results = cursor.fetchall()

capacite_totale = 0 
for i in results : 
    capacite = i[0]
    capacite_totale += capacite

print(results)
print(f"La capacité totale des salles de la plateforme est de {capacite_totale} personnes")

cursor.close()

database.close()