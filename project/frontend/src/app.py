from functions import is_name, draw_hangman, secret_word

guesses = []
misses = "Misses: "
wrong_answer_count = 0
wrong_answer_char = []
word = secret_word()
draw_hangman(wrong_answer_count)
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

done = False

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
    
    done = True
    for letter in word:
        if letter.upper() not in guesses:
            done = False

if done:
    print(f"You win! The word was {word}")
else:
    print(f"Game over! The word was {word}")