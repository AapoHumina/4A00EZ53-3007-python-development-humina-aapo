""" 
Module that has function that will return either True or False 
if given string is in name format. Name format is a string that 
contains at least 2 characters that are not numbers.
"""

import re

def is_name(name):
    """ Checks if given string is a name. Name format is a string that 
        contains at least 2 characters that are not numbers.

    Parameters
    ----------
    name_truth: `regex`
        searches if given regex match givn string
    returning_boolean : `boolean`
        converts regex to True or False boolean
    
    Exceptions
    ----------
    - If name is not a string

    Returns
    -------
    return : `True`
        returns True if string is name in  this context
    return : `False`
        returns False if name is not name in  this context
    """

    try:
        name_truth =re.search("^[A-ZÖÄÅ|a-zöäå][A-ZÖÄÅ|a-zöäå]+$", name)
        returning_boolean = bool(name_truth)
        return returning_boolean
    except:
        return False