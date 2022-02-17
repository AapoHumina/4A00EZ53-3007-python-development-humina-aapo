from string_helper import is_name, list_to_str
from user_input import ask_int, ask_name, ask

# list containing names
db = ["Hannah Smith", "Jack Smith", "Tiina Smith"]
choices = ["Add", "Insert", "Remove", "Clear"]
exit = 0
while_loop_check = True

while exit != -1:
    print(list_to_str(db))
    user_input = ask(choices)

    if user_input == -1:
        exit = -1
    elif user_input == 1:
        db.append(ask_name())
    elif user_input == 2:
        db_position = ask_int("Where to insert? :", 0, len(db))
        db.insert(db_position-1, ask_name())
    elif user_input == 3:
        db_position = ask_int("What to remove? :", 0, len(db))
        db.remove(db[db_position+1])
    elif user_input == 4:
        db.clear()