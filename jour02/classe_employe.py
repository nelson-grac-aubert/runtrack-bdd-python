import mysql.connector
from job04 import access_database, point_cursor, close_everything_properly

class Employe : 
    def __init__(self) : 

        self.__database = access_database("job07")
        self.__cursor = point_cursor(self.__database)

    def read_all_employees(self) : 

        query = """SELECT employe.id, employe.nom, employe.prenom, service.nom, employe.id_service 
                   FROM employe
                   INNER JOIN service ON employe.id_service = service.id"""

        self.__cursor.execute(query)
        results = self.__cursor.fetchall()

        print("ALL EMPLOYEES AND THEIR SERVICE ----------------")
        for id, nom, prenom, nom_service, service_id in results:
            print(f"{id}. {prenom} {nom} travaille dans le service {nom_service} (service n°{service_id})")


                    # TO DO : FIND THe FUCKING CORRECT QUERYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    def read_one_employee(self, employee_id) :

        query = f"""SELECT employe.nom, employe.prenom, service.nom, employe.id_service
                FROM employe
                INNER JOIN service ON employe.id_service = service.id
                WHERE employe.id = {employee_id};"""
        
        self.__cursor.execute(query)
        results = self.__cursor.fetchone()

        print(f"EMPLOYEE n°{employee_id} ----------------")
        print(f"{results[1]} {results[0]} travaille dans le service {results[2]} (service n°{results[3]})")

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

