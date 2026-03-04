import mysql.connector

# DATABASE UTILITIES

def access_database(database_name, host_name="localhost", user_name="root", pass_word="Misstouille83!sql"):
    """
    Connect to a MySQL database and return the connection object.
    """
    return mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=pass_word,
        database=database_name
    )

def point_cursor(database):
    """
    Return a cursor object for the given database connection.
    """
    return database.cursor()

def close_everything_properly(cursor, database):
    """
    Close cursor and database connection safely.
    """
    cursor.close()
    database.close()

# MENUS

def animal_menu():

    from job08_animal import Animal

    """
    Menu for managing animals.
    """
    a = Animal()

    while True:
        print("\n===== ANIMAL MENU =====")
        print("1. Show all animals")
        print("2. Show animals in cages")
        print("3. Add animal")
        print("4. Modify animal")
        print("5. Delete animal")
        print("0. Back")

        choice = input("Choice: ")

        if choice == "1":
            a.show_all_animals()
        elif choice == "2":
            a.show_animals_in_cages()
        elif choice == "3":
            a.create_animal()
        elif choice == "4":
            a.update_animal()
        elif choice == "5":
            a.delete_animal()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")

def cage_menu():

    from job08_cage import Cage
    
    """
    Menu for managing cages.
    """
    c = Cage()

    while True:
        print("\n===== CAGE MENU =====")
        print("1. Show all cages")
        print("2. Add cage")
        print("3. Modify cage")
        print("4. Delete cage")
        print("5. Total surface")
        print("0. Back")

        choice = input("Choice: ")

        if choice == "1":
            c.show_all_cages()
        elif choice == "2":
            c.create_cage()
        elif choice == "3":
            c.update_cage()
        elif choice == "4":
            c.delete_cage()
        elif choice == "5":
            c.total_surface()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")