from util.validation import is_date, is_email, is_personal_id, is_name
"""  
Module that contains functions for asking person for information and asking choice
"""

def ask_person():
    person_dict = {}
    input_values = {"Name": is_name,
        "Email": is_email,
        "Personal id": is_personal_id,
        "Start date at work": is_date}
    for key in input_values:
        input_bool = False
        while not input_bool:
            print(f"Give {key}")
            user_input = input()
            input_bool = input_values[key](user_input)
            if input_bool:
                person_dict[key] = user_input
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
