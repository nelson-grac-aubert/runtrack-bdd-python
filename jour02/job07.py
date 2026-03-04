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


def show_all(emp: Employe):
    emp.read_all_employees()

def show_one(emp: Employe):
    try:
        employee_id = int(input("Employee ID: "))
        emp.read_one_employee(employee_id)
    except ValueError:
        print("Invalid ID. Please enter a number.")

def create_employee(emp: Employe):
    emp.create_employee()

def delete_employee(emp: Employe):
    emp.delete_employee()

def edit_menu(emp: Employe):
    while True:
        print("\n----------- EDIT EMPLOYEE -----------")
        print("1. Edit last name")
        print("2. Edit first name")
        print("3. Edit salary")
        print("4. Edit service ID")
        print("0. Back")
        print("-------------------------------------")

        choice = input("Choose an option: ")

        if choice == "1":
            emp.edit_employee_name()
        elif choice == "2":
            emp.edit_employee_first_name()
        elif choice == "3":
            emp.edit_employee_salary()
        elif choice == "4":
            emp.edit_employee_service_id()
        elif choice == "0":
            return
        else:
            print("Invalid option.")

def main():
    emp = Employe()

    while True:
        print("\n================ EMPLOYEE MANAGEMENT ================")
        print("1. Show all employees")
        print("2. Show one employee")
        print("3. Create new employee")
        print("4. Edit employee")
        print("5. Delete employee")
        print("0. Exit")
        print("=====================================================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_all(emp)
        elif choice == "2":
            show_one(emp)
        elif choice == "3":
            create_employee(emp)
        elif choice == "4":
            edit_menu(emp)
        elif choice == "5":
            delete_employee(emp)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose a valid number.")


if __name__ == "__main__":
    main()
