import mysql.connector 

def access_database(database_name, host_name="localhost", user_name="root", pass_word="Misstouille83!sql") : 
    
    database = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = pass_word,
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

    # print(type(la_plateforme_database)) : <class 'mysql.connector.connection_cext.CMySQLConnection'>
    # print(type(la_plateforme_cursor)) : <class 'mysql.connector.cursor_cext.CMySQLCursor'>