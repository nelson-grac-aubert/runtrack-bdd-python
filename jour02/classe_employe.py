import mysql.connector
from job04 import access_database, point_cursor, close_everything_properly

class Employe : 
    def __init__(self) : 

        self.__database = access_database("job07")
        self.__cursor = point_cursor(self.__database)

    def read_all_employees(self) : 

        my_first_inner_join = """SELECT employe.nom, employe.prenom, service.nom, employe.id_service 
                             FROM employe
                             INNER JOIN service ON employe.id_service = service.id"""

        self.__cursor.execute(my_first_inner_join)
        results = self.__cursor.fetchall()

        print("---------------- ALL EMPLOYEES AND THEIR SERVICE ----------------")
        for nom, prenom, nom_service, service_id in results:
            print(f"{prenom} {nom} travaille dans le service {nom_service} (service n°{service_id})")

    def create_employee(self) : 
        pass

    def delete_employee(self) : 
        pass 

    def edit_employee_name(self) : 
        pass
    def edit_employee_first_name(self) : 
        pass
    def edit_employee_salary(self) : 
        pass
    def edit_employee_service_id(self) : 
        pass

employee_crud = Employe()
employee_crud.read_all_employees()