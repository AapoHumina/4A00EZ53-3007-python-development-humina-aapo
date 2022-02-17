"""
Module that contains functions for asking a int, asking a name and asking a choice
"""

from string_helper import is_name

def ask_int(message, min , max):
    """ Ask a int in given range

    Parameters
    ----------
    message : `string`
        printed string for asking int
    min : `int`
        minimun number in range
    max : `int`
        maximun number in range
    r : `range`
        minimun-maximum range
    number : `input`
        user given argument, excepting int
    Exceptions
    ----------
    - If message is not string
    - If min is not int
    - If max is not int
    - If min is higher number than max

    Returns
    -------
    return : number
        if number is in r range, returns number, otherwise asks again
    """
    if not isinstance(message, (str)):
        raise Exception("message should be a string")
    if not isinstance(min, (int)):
        raise Exception("min should be a int")
    if not isinstance(max, (int)):
        raise Exception("max should be a int")
    if max < min:
        raise Exception("max should be higher number than min")
    r = range(min,max+1)
    while True:
        print(message, end = " ")
        number = int(input())
        if number in r:
            return number
        else:
            print(f"Number must be between {min}-{max}")

def ask_name(message="Give name: "):
    """ Asks a name

    Parameters
    ----------
    message = `string`
        given string for asking name
    while_loop_check : `boolean`
        keeps while loop running
    name : `input`
        user given name, excepting string

    Exceptions
    ----------
    - If message is not string

    Returns
    -------
    return : name
        returns user given name if it is proper name
    """
    if not isinstance(message, (str)):
        raise Exception("message should be a string")
    while_loop_check = True
    while while_loop_check:
        print(message, end = "")
        name = input()
        if is_name(name):
           return name
        else:
            print("Please give a proper name: Firstname Lastname.")

def ask(choices):
    """ Prints a menu and asks users choice 

    Parameters
    ----------
    choices = `list`
        given list of strings
    menu_list : `string`
        string for keeping all the strings in choices list
    choice : `input`
        user given input, excepting int

    Exceptions
    ----------
    - If choices is not a list
    - If list is empty

    Returns
    -------
    return : choice
        returns user given number if it is in given range
    """
    if not isinstance(choices, (list)):
        raise Exception("choices should be a list")
    if len(choices) == 0:
        raise Exception("choices list should never be a empty")
    menu_list = "Menu:"
    for index in range(0, len(choices)):
        menu_list =menu_list + "\n" + f"{index+1}: " + choices[index]
    menu_list = menu_list + "\n" + "0: Exit"
    print(menu_list)
    while True:
        print("Your choice: ", end = "")
        choice = int(input())
        if choice == 0:
            return -1
        for index in range(0, len(choices)):
            if choice == index+1:
                return choice
        print(f"Please give number between 1-{len(choices)}")