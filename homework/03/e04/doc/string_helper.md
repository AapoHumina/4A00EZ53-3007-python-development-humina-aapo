Module string_helper
====================
Module that contains functions

Functions
---------

    
`is_name(name, ignore_case)`
:   Checks if given name is a name and if it is properly capitalized
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
    Returns
    -------
    return : `True`
        returns True if name is properly capitalized name or a name
    return : `False`
        returns False if name is not properly capitalized or not a name at all