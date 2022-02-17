from string_helper import is_name

def ask_int(message, min, max):
    while 1 > 0:
        print("Give grade:", end = " ")
        number = int(input())
        if number == 4:
            return number
        elif number == 5:
            return number
        elif number == 6:
            return number
        elif number == 7:
            return number
        elif number == 8:
            return number
        elif number == 9:
            return number
        elif number == 10:
            return number
        else:
            print(f"Number must be between {min}-{max}")
            continue
def ask_name(message):
    while_loop_check = True
    while while_loop_check:
        print("Give name: ", end = "")
        name = input()
        if is_name(name):
           return name
        else:
            print("Please give a proper name: Firstname Lastname.")
def ask(choices):
    choice = "4"
    print("Menu:")
    print(f"1: {choices[0]}")
    print(f"2: {choices[1]}")
    print(f"3: {choices[2]}")
    print(f"4: {choices[3]}")
    print(f"0: {choices[4]}")
    print("")
    while True:
        print("Your choice: ", end ="")
        choice = int(input())
        if choice == int(choice) and choice > 0 and choice < len(choices):
            return choice
        elif choice == 0:
            return -1
        else:
            print("Value must be between 1-4 or 0")


print(ask(["Add", "Insert", "Remove", "Clear", "Exit"]))