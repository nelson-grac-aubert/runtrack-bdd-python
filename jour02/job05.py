import mysql.connector 
from job04 import access_database, point_cursor, close_everything_properly

def get_total_surface(cursor) : 

    cursor.execute("SELECT superficie FROM etage")

    results = cursor.fetchall()

    total_surface = 0
    for element in results : 
        singular_surface = element[0]
        total_surface += singular_surface

    print(f"La superficie totale de la plateforme est {total_surface} m2")
    return total_surface 

if __name__ == "__main__" : 

    la_plateforme_database = access_database("LaPlateforme")
    la_plateforme_cursor = point_cursor(la_plateforme_database)
    get_total_surface(la_plateforme_cursor)
    close_everything_properly(la_plateforme_cursor, la_plateforme_database)