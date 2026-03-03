import mysql.connector
from job04 import access_database, point_cursor, close_everything_properly

class Employe : 
    def __init__(self) : 

        self.__database = access_database("job07")
        self.__cursor = point_cursor(self.__database)

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
