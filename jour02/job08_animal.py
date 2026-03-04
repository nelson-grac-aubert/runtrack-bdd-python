from job08_menu import access_database, point_cursor, close_everything_properly

class Animal:
    """
    CRUD manager for the 'animal' table.
    """

    def __init__(self):
        self.db = access_database("myzoo")
        self.cursor = point_cursor(self.db)

    def input(self, msg, expected_type=str):
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

    def create_animal(self):
        name = self.input("Animal name: ")
        race = self.input("Race: ")
        cage_id = self.input("Cage ID: ", int)
        birth = self.input("Birth date (YYYY-MM-DD): ")
        country = self.input("Country of origin: ")

        query = """
            INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, (name, race, cage_id, birth, country))
        self.db.commit()
        print("Animal added.")

    def show_all_animals(self):
        self.cursor.execute("SELECT * FROM animal")
        for row in self.cursor.fetchall():
            print(f"#{row[0]} : {row[1]}, a {row[2]} born on the {row[3]} in {row[5]}, living in cage #{row[4]}")

    def show_animals_in_cages(self):
        query = """
            SELECT cage.id, cage.superficie, animal.nom, animal.race
            FROM cage
            LEFT JOIN animal ON cage.id = animal.cage_id
            ORDER BY cage.id
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print("\nANIMALS BY CAGE ----------------")
        for cage_id, superficie, name, race in results:
            if name:
                print(f"Cage {cage_id} ({superficie} m²): {name} ({race})")
            else:
                print(f"Cage {cage_id} ({superficie} m²): EMPTY")

    def update_animal(self):
        animal_id = self.input("Animal ID: ", int)

        print("\n1. Name\n2. Race\n3. Cage ID\n4. Birth date\n5. Country")
        choice = self.input("Field: ")

        fields = {
            "1": ("nom", str),
            "2": ("race", str),
            "3": ("id_cage", int),
            "4": ("date_naissance", str),
            "5": ("pays_origine", str)
        }

        if choice not in fields:
            print("Invalid choice.")
            return

        column, t = fields[choice]
        new_value = self.input(f"New {column}: ", t)

        query = f"UPDATE animal SET {column} = %s WHERE id = %s"
        self.cursor.execute(query, (new_value, animal_id))
        self.db.commit()

        print("Animal updated.")

    def delete_animal(self):
        animal_id = self.input("Animal ID: ", int)
        self.cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))
        self.db.commit()
        print("Animal deleted.")