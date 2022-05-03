import random
import re

def menu():
  menu ="""Main Menu:
1: Play Hangman
2: Look at High Score
0: Exit
"""
  return menu
def is_name(name):
    try:
        check = re.search("^[A-ZÄÖÅ][a-zäöå]+$", name)
        if bool(check):
            return True
        else:
            return False
    except:
        return False

def draw_hangman(count):
    if count == 0:
        print("""      ________      
      |      |      
      |             
      |             
      |             
    __|______       
    |       | """)
    elif count == 1:
        print("""      ________      
      |      |      
      |      O      
      |             
      |             
    __|______       
    |       | """)
    elif count == 2:
        print("""      ________      
      |      |      
      |      O      
      |      |      
      |             
    __|______       
    |       | """)
    elif count == 3:
        print("""      ________      
      |      |      
      |      O      
      |      |      
      |     /       
    __|______       
    |       | """)
    elif count == 4:
        print("""      ________      
      |      |      
      |      O      
      |      |      
      |     / \      
    __|______       
    |       | """)
    elif count == 5:
        print("""      ________      
      |      |      
      |    __O      
      |      |      
      |     / \      
    __|______       
    |       | """)
    elif count == 6:
        print("""      ________      
      |      |      
      |    __O__    
      |      |      
      |     / \      
    __|______       
    |       | """)

def secret_word():
    f = open("wordlist.txt", "r")
    text = f.read()
    wordlist = text.split("\n")
    hiddenword = wordlist[(random.randrange(0,len(wordlist)))]
    f.close
    return hiddenword

def save_h_score(name, word, score):
  f = open("highscore.txt", "a")
  f.write(f"{word}:\n{name} {score} seconds\n")
  f.close

def show_h_score():
  f = open("highscore.txt", "r")
  return f.read()

def is_letter(letter):
  abc = re.search("^[A-ZÄÖÅa-zäöå]$", letter)
  if bool(abc):
    return True
  else:
    return False

def is_number012(number):
  number_truth = re.search("^[012]$", number)
  if bool(number_truth):
    return True
  else:
    return False