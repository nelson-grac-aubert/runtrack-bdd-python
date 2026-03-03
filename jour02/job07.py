import mysql.connector 
from job04 import access_database, point_cursor, close_everything_properly
from classe_employe import Employe

def get_rich_employees(cursor) : 

    cursor.execute("SELECT nom, prenom FROM employe WHERE salaire > 3000")

    results = cursor.fetchall()

    print("---------------- RICH EMPLOYEES ---------------------------------")
    for element in results : 
        print(f"{element[1]} {element[0]} gagne plus de 3000e par mois")

def get_all_employees_with_service_id(cursor):

    my_first_inner_join = """SELECT employe.nom, employe.prenom, service.nom 
                             FROM employe
                             INNER JOIN service ON employe.id_service = service.id"""

    cursor.execute(my_first_inner_join)
    results = cursor.fetchall()

    print("---------------- ALL EMPLOYEES AND THEIR SERVICE ----------------")
    for nom, prenom, nom_service in results:
        print(f"{prenom} {nom} travaille dans le service {nom_service}")

def get_all_employees_with_service_name(cursor):

    my_first_inner_join = """SELECT employe.nom, employe.prenom, service.nom 
                             FROM employe
                             INNER JOIN service ON employe.id_service = service.id"""

    cursor.execute(my_first_inner_join)
    results = cursor.fetchall()

    print("---------------- ALL EMPLOYEES AND THEIR SERVICE ----------------")
    for nom, prenom, nom_service in results:
        print(f"{prenom} {nom} travaille dans le service {nom_service}")


if __name__ == "__main__" : 

    job07_database = access_database("job07")
    job07_cursor = point_cursor(job07_database)
    # get_rich_employees(job07_cursor)
    # get_all_employees_with_service_name(job07_cursor)

    employee_crud = Employe()
    employee_crud.read_all_employees()
    employee_crud.read_one_employee(2)

    close_everything_properly(job07_cursor, job07_database)