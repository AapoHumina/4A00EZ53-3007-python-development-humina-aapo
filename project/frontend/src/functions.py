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


def menu():
    print("n")
