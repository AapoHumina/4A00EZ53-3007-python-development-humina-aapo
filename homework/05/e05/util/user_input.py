from util.validation import is_date, is_email, is_personal_id, is_name
"""  
Module that contains functions for asking person for information and asking choice
"""

def ask_person():
    """ 
    Aska a person for their name, email, personal id and start date at work

    Parameters
    ----------
    name_true = `bool`
        boolean for keeping loop goin until user given valid answer
    email_true = `bool`
        boolean for keeping loop goin until user given valid answer
    id_true = `bool`
        boolean for keeping loop goin until user given valid answer
    date_true = `bool`
        boolean for keeping loop goin until user given valid answer
    person_dict : `dict`
        directory for holding the given information and what is returned
    name = `string`
        user given name
    email = `string`
        user given email
    id = `string`
        user given id
    date = `string`
        user given date

    Returns
    -------
    return : person_dict `dict` 
        returns user given string in a directory
    """
    name_true = False
    email_true = False
    id_true = False
    date_true = False
    person_dict = {}

    while not name_true:
        print("Give Name: ", end = "")
        name = input()
        name_true = is_name(name)
        if name_true:
            person_dict["Name"] = name
    while not email_true:
        print("Give Email: ", end = "")
        email = input()
        email_true = is_email(email)
        if email_true:
            person_dict["Email"] = email
    while not id_true:
        print("Give Personal ID: ", end = "")
        id = input()
        id_true = is_personal_id(id)
        if id_true:
            person_dict["Personal ID"] = id
    while not date_true:
        print("Give Start Date at the Work: ", end = "")
        date = input()
        date_true = is_date(date)
        if date_true:
            person_dict["Start Date at work"] = date
    return person_dict

def ask(choices):
    """ Prints a menu and asks users choice 

    Parameters
    ----------
    choices = `list`
        given list of strings
    menu_list : `string`
        string for keeping all the strings in choices list
    invalid_choice : `bool`
        toggle to keep loop running until valid numbers are given
    choice : `input`
        user given input, excepting int

    Exceptions
    ----------
    - If choices is not a list
    - If list is empty

    Returns
    -------
    return : choice
        returns user given number -1 if it is in given range
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
    invalid_choice = True
    while invalid_choice:
        try:
            print("Your choice: ", end = "")
            choice = int(input())
            if choice >= 0 and choice <= len(choices):
                invalid_choice = False
            else:
                print(f"Please give number between 1-{len(choices)}")
        except:
            print("Please give numbers")
    return choice-1
