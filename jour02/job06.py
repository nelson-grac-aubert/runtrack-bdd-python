import mysql.connector 
from job04 import access_database, point_cursor, close_everything_properly

def get_total_capacity(cursor) : 
    
    cursor.execute("SELECT SUM(capacite) FROM salle")

    total_capacity = cursor.fetchone()[0]

    print(f"La capacité totale des salles de la plateforme est de {total_capacity} personnes")

if __name__ == "__main__" : 

    la_plateforme_database = access_database("LaPlateforme")
    la_plateforme_cursor = point_cursor(la_plateforme_database)
    get_total_capacity(la_plateforme_cursor)
    close_everything_properly(la_plateforme_cursor, la_plateforme_database)