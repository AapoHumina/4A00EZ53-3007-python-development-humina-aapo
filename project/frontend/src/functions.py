import random
import time
import re

def is_name(name):
    try:
        check = re.search("^[A-ZÖÅ][a-zäöå]+$", name)
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