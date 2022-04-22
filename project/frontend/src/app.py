import time
from functions import is_name, draw_hangman, secret_word, menu, save_h_score, show_h_score

guesses = []
misses = "Misses: "
wrong_answer_count = 0
wrong_answer_char = []
word = secret_word()
stop = False

while not stop:
        
    print(menu())
    menu_choice = int(input())
    if menu_choice == 2:  
        print(show_h_score())

    elif menu_choice == 1:
        print("Let's play HANGMAN!")
        draw_hangman(wrong_answer_count)

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

            guess = input()
            guesses.append(guess.upper())
            if guess.upper() not in word.upper():
                if wrong_answer_count == 0:
                    misses = misses + guess.upper()
                else:
                    misses = misses + ", " + guess.upper()
                wrong_answer_count = wrong_answer_count + 1
                draw_hangman(wrong_answer_count)
                print(misses)
                if wrong_answer_count == 7:
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
            print(f"You win! The word was {word}. You found the word in {round(score, 2)} seconds")
            
        else:
            print(f"Game over! The word was {word}")
    else:
        print("Bye Bye :3")
        stop = True