"""
Module that contains functions for checking name and making a list a string
"""

def is_name(name, ignore_case=False):
    """ Checks if given name is a name and if it is properly capitalized
    Parameters
    ----------
    name : `string`
        user given name
    ignore_case : `boolean`
        checks do we ignore case or not
    name_list : `list`
        name split from " " to create list with first_name and last_name in it
    first_name : `string`
        first name from the name user has given
    last_name : `string`
        last name from the name user has given
    name1_list : `list`
        name split from "-" to create list with first_name and first1_name in it
    first1_name : `string`
        second first name if users first name has two names example(Ville-Kalle)
    
    Exceptions
    ----------
    - If name is not a string
    - If ignore_case is not boolean

    Returns
    -------
    return : `True`
        returns True if name is properly capitalized name or if ignore_case true returns a name without caring about uppercase or lowercase
    return : `False`
        returns False if name is not properly capitalized or not a name at all
    """
    if name != str(name):
        raise Exception("title should be string")
    if ignore_case != bool(ignore_case):
        raise Exception("ignore_case should be boolean")
    first1_name = "Pekka"
    if ignore_case:
        if name.rfind(" ") == -1 or name.count(" ") > 1:
            return False
        elif name.count("-") == 1:
            if name[0] == "-" or name[0] == " " or name[len(name)-1] == "-" or name[len(name)-1] == "-":
                return False
            name_list= name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
            name1_list= first_name.split("-")
            first_name = name1_list[0]
            first1_name = name1_list[1]
        else:
            if name[0] == " " or name[len(name)-1] == "-":
                return False
            name_list= name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
        if first_name.isalpha() == False or first1_name.isalpha() == False or last_name.isalpha() == False:
            return False
        elif len(first_name) >= 2 and len(first1_name) >= 2 and len(last_name) >= 2:
            return True
    else:
        if name.rfind(" ") == -1 or name.count(" ") > 1:
            return False
        elif name.count("-") == 1:
            if name[0] == "-" or name[0] == " " or name[len(name)-1] == "-" or name[len(name)-1] == "-":
                return False
            name_list= name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
            name1_list= first_name.split("-")
            first_name = name1_list[0]
            first1_name = name1_list[1]
        else:
            if name[0] == " " or name[len(name)-1] == "-":
                return False
            name_list= name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
        for index in range(1, len(first_name)):
            if first_name[index] == first_name[index].capitalize():
                return False
        for index in range(1, len(last_name)):
            if last_name[index] == last_name[index].capitalize():
                return False
        for index in range(1, len(first1_name)):
            if first1_name[index] == first1_name[index].capitalize():
                return False
        if first_name.isalpha() == False or first1_name.isalpha() == False or last_name.isalpha() == False:
            return False
        elif first_name.islower() or first1_name.islower() or last_name.islower():
            return False
        elif first_name[0] == first_name[0].capitalize() and first1_name[0] == first1_name[0].capitalize() and last_name[0] == last_name[0].capitalize() and len(first_name) >= 2 and len(first1_name) >= 2 and len(last_name) >= 2:
            return True

def list_to_str(my_list):
    """ Converts a list to a string

    Parameters
    ----------
    my_list : `list`
        received list of strings
    name_list : `list`
        parameter where strings in a list are stored as a string

    Exceptions
    ----------
    - If my_list is not a list

    Returns
    -------
    return : namelist
        returns names in a list as a string
    return : "Empty List"
        returns string "Empty List" if list is empty
    """
    if not isinstance(my_list, (list)):
        raise Exception("my_list should be a list")
    if len(my_list) == 0:
        return "Empty List"
    name_list = "Database:"
    for index in range(0, len(my_list)):
        name_list =name_list + "\n" + f"{index+1}: " + my_list[index]
    return name_list