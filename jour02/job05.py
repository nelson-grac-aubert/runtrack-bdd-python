import mysql.connector 

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Misstouille83!sql",
    database="LaPlateforme"
)

cursor = database.cursor()

cursor.execute("SELECT superficie FROM etage")

results = cursor.fetchall()

superficie = 0
for i in results : 
    surface = i[0]
    superficie += surface

print(results)
print(f"La superficie totale de la plateforme est {superficie} m2")

cursor.close()

database.close()