students = []


try:
    with open("students.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            students.append((name, marks))
except FileNotFoundError:
    pass


while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")


    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        students.append((name, marks))


        with open("students.txt", "a") as file:
            file.write(name + "," + marks + "\n")

    elif choice == "2":
        print("\nStudent List:")
        with open("students.txt", "r") as file:
            data = file.readlines()
            for line in data:
                print(line.strip())

    
    elif choice == "3":
        search = input("Enter name: ")
        found = False

        for student in students:
            if student[0] == search:
                print("Found:", student)
                found = True
                break

        if not found:
            print("Not Found")


    elif choice == "4":
        delete = input("Enter name: ")
        new_students = []
        found = False

        for student in students:
            if student[0] != delete:
                new_students.append(student)
            else:
                found = True

        students = new_students

        with open("students.txt", "w") as file:
            for student in students:
                file.write(student[0] + "," + student[1] + "\n")

        if found:
            print("Deleted successfully")
        else:
            print("Not Found")


    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")