from functions import is_name

print("Let's play HANGMAN!")
name_check = False
while name_check == False:
    print("What is your name?")
    username = input()
    name_check = is_name(username)
    if name_check:
        print(f"Welcome {username}")
    else:
        print("Please give proper name with at least 2 characters")
        print("first character uppercase, no numbers (for example Jussi)")