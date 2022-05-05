import time
from functions import is_name, draw_hangman, secret_word, menu, save_h_score, show_h_score, is_letter, is_number012

stop = False
username = ""

while not stop:

    guesses = []
    misses = "Misses: "
    wrong_answer_count = 0
    wrong_answer_char = []
    word = secret_word()
    number_truth = False

    while not number_truth:
        print(menu())
        menu_choice = input()
        number_truth = is_number012(str(menu_choice))
        if number_truth:
            menu_choice= int(menu_choice)    
            if menu_choice == 2:  
                print(show_h_score())

            elif menu_choice == 1:
                print("Let's play HANGMAN!")
                draw_hangman(wrong_answer_count)

                name_check = False
                while name_check == False:
                    if username == "":
                        print("What is your name?")
                        username = input()
                    name_check = is_name(username)
                    if name_check:
                        print(f"Welcome {username}")
                    else:
                        print("Please give proper name with at least 2 characters")
                        print("first character uppercase, no numbers (for example Jussi)")

                done = False
                print("Try to guess the secret word one letter at a time")
                start = time.time()
                while not done:
                    for letter in word:
                        if letter.upper() in guesses:
                            print(letter, end = " ")
                        else:
                            print("_", end = " ")
                    print("")

                    correct_input = False
                    while not correct_input:
                        guess = input()
                        correct_input = is_letter(guess)
                        if not correct_input:
                            print("Please give only one character and only letters (abc...zäöå)")

                    guesses.append(guess.upper())
                    if guess.upper() not in word.upper():
                        if wrong_answer_count == 0:
                            misses = misses + guess.upper()
                        else:
                            misses = misses + ", " + guess.upper()
                        wrong_answer_count = wrong_answer_count + 1
                        draw_hangman(wrong_answer_count)
                        print(misses)
                        if wrong_answer_count == 6:
                            break
                    else:
                        print("That's right!")
                    
                    done = True
                    for letter in word:
                        if letter.upper() not in guesses:
                            done = False
                end = time.time()
                score =end - start
                if done:
                    save_h_score(username, word, round(score, 2))
                    guesses = []
                    print(f"You win! The word was {word}. You found the word in {round(score, 2)} seconds")
                    
                else:
                    guesses = []
                    print(f"Game over! The word was {word}")
            else:
                print("Bye Bye")
                stop = True
        else:
            print("Please choose with number 0, 1 or 2")