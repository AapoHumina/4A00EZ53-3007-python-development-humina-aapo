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
  check = True
  d = open("highscore.txt", "r")
  content = d.read()
  if not content == "":
    high_score_list = csv_to_list(content)
    high_score_list_sorted = sorted(high_score_list, reverse=False)
    count = 0
    for hscore_word in high_score_list_sorted:
      if hscore_word[0] == word:
        print(hscore_word[2])
        count = count +1
        if count == 3:
          check = False
          if float(hscore_word[2]) > float(score):
            hscore_word == (f"{word}:{name}:{score}")
            count = 0
    d.close
  if check:
    f = open("highscore.txt", "a")
    f.write(f"{word}:{name}:{score}\n")
    f.close

def show_h_score():
  f = open("highscore.txt", "r")
  content = f.read()
  content_str = csv_to_list(content)
  content_sorted = sorted(content_str, reverse=False)
  f.close
  return content_sorted

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

def csv_to_list(csv):
  result = []
  lines = csv.strip().split("\n") 
  for line in lines:
      result.append(line.split(":")) 
  return(result)
