"""
Module that contains functions
"""

def is_name(name):
    """ Checks if given name is a name and if it is properly capitalized
    Parameters
    ----------
    name : `string`
        user given name
    name_list : `list`
        name split from " " to create list with first_name and last_name in it
    first_name : `string`
        first name from the name user has given
    last_name : `string`
        last name from the name user has given
    Returns
    -------
    return : `True`
        returns True if name is properly capitalized name
    return : `False`
        returns False if name is not properly capitalized or not a name at all
    """
    if name.rfind(" ") == -1:
        return False
    else:
        name_list= name.split(" ")
        first_name = name_list[0]
        last_name = name_list[1]
    if first_name.isalpha() == False or last_name.isalpha() == False:
        return False
    elif first_name.islower() or last_name.islower():
        return False
    elif first_name.isupper() or last_name.isupper():
        return False
    elif first_name[0] == first_name[0].capitalize() and last_name[0] == last_name[0].capitalize() and len(first_name) >= 2 and len(last_name) >= 2:
        return True