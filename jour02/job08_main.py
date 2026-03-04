from job08_menu import animal_menu, cage_menu

def main():
    while True:
        print("\n========== ZOO MANAGEMENT ==========")
        print("1. Manage animals")
        print("2. Manage cages")
        print("0. Exit")
        print("====================================")

        choice = input("Choice: ")

        if choice == "1":
            animal_menu()
        elif choice == "2":
            cage_menu()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()