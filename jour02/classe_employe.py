import mysql.connector
from job04 import access_database, point_cursor, close_everything_properly

class Employe:
    """
    Class providing CRUD operations for the 'employe' table in a MySQL database.
    """

    def __init__(self):
        """
        Initialize the database connection and cursor.
        """
        self.__database = access_database("job07")
        self.__cursor = point_cursor(self.__database)

    def read_all_employees(self):
        """
        Display all employees along with their associated service.
        """
        query = """
            SELECT employe.id, employe.nom, employe.prenom, service.nom, employe.id_service
            FROM employe
            INNER JOIN service ON employe.id_service = service.id
        """

        self.__cursor.execute(query)
        results = self.__cursor.fetchall()

        print("ALL EMPLOYEES AND THEIR SERVICE ----------------")
        for id, nom, prenom, nom_service, service_id in results:
            print(f"{id}. {prenom} {nom} works in service {nom_service} (service #{service_id})")

    def read_one_employee(self, employee_id):
        """
        Display information about a specific employee.

        Parameters:
            employee_id (int): ID of the employee to display.
        """
        query = """
            SELECT employe.nom, employe.prenom, service.nom, employe.id_service
            FROM employe
            INNER JOIN service ON employe.id_service = service.id
            WHERE employe.id = %s
        """

        self.__cursor.execute(query, (employee_id,))
        results = self.__cursor.fetchone()

        if results:
            print(f"EMPLOYEE #{employee_id} ----------------")
            print(f"{results[1]} {results[0]} works in service {results[2]} (service #{results[3]})")
        else:
            print("No employee found with this ID.")

    def get_user_input(self, displayed_message: str, expected_type=str):
        """
        Ask the user for input and validate the type.

        Parameters:
            displayed_message (str): Message displayed to the user.
            expected_type (type): Expected Python type (str, int, float).

        Returns:
            Any: The validated user input.
        """
        while True:
            value = input(displayed_message)

            if expected_type == str:
                if value.strip() == "":
                    print("Input cannot be empty.")
                    continue
                return value.strip()

            try:
                return expected_type(value)
            except ValueError:
                print(f"Invalid input. Expected a value of type {expected_type.__name__}.")

    def create_employee(self):
        """
        Create a new employee in the database.
        Asks the user for: name, first name, salary, service ID.
        """
        nom = self.get_user_input("Employee last name: ", str)
        prenom = self.get_user_input("Employee first name: ", str)
        salaire = self.get_user_input("Salary: ", float)
        id_service = self.get_user_input("Service ID: ", int)

        query = """
            INSERT INTO employe (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        """

        self.__cursor.execute(query, (nom, prenom, salaire, id_service))
        self.__database.commit()

        print("New employee successfully added.")

    def delete_employee(self):
        """
        Delete an employee from the database based on their ID.
        """
        employee_id = self.get_user_input("ID of the employee to delete: ", int)

        query = "DELETE FROM employe WHERE id = %s"

        self.__cursor.execute(query, (employee_id,))
        self.__database.commit()

        print(f"Employee #{employee_id} has been deleted.")

    def select_employee_for_modificatiion(self):
        """
        Ask the user which employee they want to modify.

        Returns:
            int: ID of the selected employee.
        """
        return self.get_user_input("ID of the employee to modify: ", int)

    def edit_employee_name(self):
        """
        Update the last name of an employee.
        """
        employee_id = self.select_employee_for_modificatiion()
        new_name = self.get_user_input("New last name: ", str)

        query = "UPDATE employe SET nom = %s WHERE id = %s"

        self.__cursor.execute(query, (new_name, employee_id))
        self.__database.commit()

        print("Last name successfully updated.")

    def edit_employee_first_name(self):
        """
        Update the first name of an employee.
        """
        employee_id = self.select_employee_for_modificatiion()
        new_first_name = self.get_user_input("New first name: ", str)

        query = "UPDATE employe SET prenom = %s WHERE id = %s"

        self.__cursor.execute(query, (new_first_name, employee_id))
        self.__database.commit()

        print("First name successfully updated.")

    def edit_employee_salary(self):
        """
        Update the salary of an employee.
        """
        employee_id = self.select_employee_for_modificatiion()
        new_salary = self.get_user_input("New salary: ", float)

        query = "UPDATE employe SET salaire = %s WHERE id = %s"

        self.__cursor.execute(query, (new_salary, employee_id))
        self.__database.commit()

        print("Salary successfully updated.")

    def edit_employee_service_id(self):
        """
        Update the service ID of an employee.
        """
        employee_id = self.select_employee_for_modificatiion()
        new_service_id = self.get_user_input("New service ID: ", int)

        query = "UPDATE employe SET id_service = %s WHERE id = %s"

        self.__cursor.execute(query, (new_service_id, employee_id))
        self.__database.commit()

        print("Service ID successfully updated.")