from util.user_input import ask_person, ask


def main():
    employees = []
    input = 1
    while input != -1:
        print("Employees", employees)
        input = ask(["Add"])
        if input == 0:
            employee = ask_person()
            employees.append(employee)

main()