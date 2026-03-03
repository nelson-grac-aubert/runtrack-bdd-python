import mysql.connector 

def access_database(database_name) : 

    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Misstouille83!sql",
        database = database_name
    )

    return database

def point_cursor(database) : 

    return database.cursor()

def get_name_and_capacities(cursor) : 

    cursor.execute("SELECT nom, capacite FROM salle")
    results = cursor.fetchall()
    print(results)

    return results

def close_everything_properly(cursor, database) : 

    cursor.close()
    database.close()

if __name__ == "__main__" : 

    la_plateforme_database = access_database("LaPlateforme")
    la_plateforme_cursor = point_cursor(la_plateforme_database)
    get_name_and_capacities(la_plateforme_cursor)
    close_everything_properly(la_plateforme_cursor, la_plateforme_database)