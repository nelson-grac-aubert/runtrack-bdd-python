import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Misstouille83!sql" 
        )
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE myzoo")
        print("Base de données 'myzoo' créée avec succès.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("La base de données 'myzoo' existe déjà.")
        else:
            print(f"Erreur lors de la création de la base : {err}")

    finally:
        cursor.close()
        connection.close()


def create_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Misstouille83!sql",
            database="myzoo"
        )
        cursor = connection.cursor()

        TABLES = {}

        TABLES["cage"] = (
            """
            CREATE TABLE IF NOT EXISTS cage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                superficie INT NOT NULL,
                capacite INT NOT NULL
            );
            """
        )

        TABLES["animal"] = (
            """
            CREATE TABLE IF NOT EXISTS animal (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                race VARCHAR(255),
                date_naissance VARCHAR(255),
                cage_id INT,
                pays_origine, VARCHAR(255),
                FOREIGN KEY (cage_id) REFERENCES cage(id)
            );
            """
        )

        for name, query in TABLES.items():
            cursor.execute(query)
            print(f"Table '{name}' vérifiée/créée.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la création des tables : {err}")

if __name__ == "__main__":
    create_database()
    create_tables()