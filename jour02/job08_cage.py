from job08_menu import access_database, point_cursor

class Cage:
    """
    CRUD manager for the 'cage' table.
    """

    def __init__(self):
        self.db = access_database("myzoo")
        self.cursor = point_cursor(self.db)

    def _input(self, msg, expected_type=str):
        while True:
            value = input(msg)
            if expected_type == str:
                if value.strip() == "":
                    print("Input cannot be empty.")
                    continue
                return value.strip()
            try:
                return expected_type(value)
            except ValueError:
                print(f"Expected {expected_type.__name__}.")

    def create_cage(self):
        superficie = self._input("Surface (m²): ", float)
        capacite = self._input("Max capacity: ", int)

        query = "INSERT INTO cage (superficie, capacite) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite))
        self.db.commit()

        print("Cage created.")


    def show_all_cages(self):
        self.cursor.execute("SELECT * FROM cage")
        for row in self.cursor.fetchall():
            print(f"#{row[0]} : a cage of {row[1]} square meters with a capacity of {row[2]}")

    def total_surface(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        total = self.cursor.fetchone()[0]
        print(f"Total cage surface: {total} m²")

    def update_cage(self):
        cage_id = self._input("Cage ID: ", int)

        print("\n1. Surface\n2. Max capacity")
        choice = self._input("Field: ")

        if choice == "1":
            new_value = self._input("New surface: ", float)
            column = "superficie"
        elif choice == "2":
            new_value = self._input("New capacity: ", int)
            column = "capacite_max"
        else:
            print("Invalid choice.")
            return

        query = f"UPDATE cage SET {column} = %s WHERE id = %s"
        self.cursor.execute(query, (new_value, cage_id))
        self.db.commit()

        print("Cage updated.")

    def delete_cage(self):
        cage_id = self._input("Cage ID: ", int)
        self.cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))
        self.db.commit()
        print("Cage deleted.")