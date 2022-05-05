"""

Module that has the functions of the game

"""
import random
import re

def menu():
  """
  Just returns menu

  Parameters
  ----------
  menu : `string`
    string of menu

  Returns
  -------
  return : `string`
    returns menu string to be printed
  """
  menu ="""Main Menu:
1: Play Hangman
2: Look at High Score
0: Exit
"""
  return menu

def is_name(name):
  """
  Checks if user given name is a name

  Parameters
  ----------
  name : `string`
    name to be checked
  check : `regex`
    regex to check if name is at least 2 characters long

  Returns
  -------
  return : `bool`
    returns true or false if name is proper name or not
  """
  try:
      check = re.search("^[A-ZÄÖÅ][a-zäöå]+$", name)
      if bool(check):
          return True
      else:
          return False
  except:
      return False

def draw_hangman(count):
  """
  Prints hangman ASCII art

  Parameters
  ----------
  count : `int`
    number of wrong answers
  """
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
  """
  Takes a random word from textfile

  Parameters
  ----------

  text : `string`
    textfile insides converted to string
  wordlist : `list`
    text string converted to list on \n
  Returns
  -------
  return : `string`
    returns randomly selected word
  """
  f = open("wordlist.txt", "r")
  text = f.read()
  wordlist = text.split("\n")
  hiddenword = wordlist[(random.randrange(0,len(wordlist)))]
  f.close
  return hiddenword

def save_h_score(name, word, score):
  """
  Saves the score to textfile

  Parameters
  ----------

  check : `bool`
    boolean to check if new score gets added
  content : `string`
    highscore textfile in string form
  high_score_list = `list`
    makes the file string into list
  high_score_list_sorted = `list`
    sorted list
  count = `int`
    count the number of times word is in highscore textfile

  """
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
  """
  Shows highscores from textfile highscore

  Parameters
  ----------

  content : `string`
    highscore textfile in string form
  content_list : `list`
    text string converted to list on \n
  content_sorted : `list`
    content_list sorted

  Returns
  -------
  return : `list`
    returns highscore sorted
  """
  f = open("highscore.txt", "r")
  content = f.read()
  content_list = csv_to_list(content)
  content_sorted = sorted(content_list, reverse=False)
  f.close
  return content_sorted

def is_letter(letter):
  """
  Checks if user given letter is letter

  Parameters
  ----------
  letter : `user input`
    user input
  abc : `regex`
    searches for proper letters 

  Returns
  -------
  return : `bool`
    returns true or false if letter is proper letter or not
  """
  abc = re.search("^[A-ZÄÖÅa-zäöå]$", letter)
  if bool(abc):
    return True
  else:
    return False

def is_number012(number):
  """
  Checks if user given number is 012

  Parameters
  ----------
  number : `user input`
    user input
  number_truth : `regex`
    searches for proper letters 

  Returns
  -------
  return : `bool`
    returns true or false if number is 0 1 2 or not
  """
  number_truth = re.search("^[012]$", number)
  if bool(number_truth):
    return True
  else:
    return False

def csv_to_list(csv):
  """
  Transforms given csv string (word, name, score) into a 2d list.

  Parameters
  ----------
  csv : `str`
    csv file containing high score

  Returns
  -------
  return : `list`
    2D list containing highscores
  """
  result = []
  lines = csv.strip().split("\n") 
  for line in lines:
      result.append(line.split(":")) 
  return(result)
