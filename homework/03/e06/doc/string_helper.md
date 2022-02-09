Module string_helper
====================
Module that contains functions

Functions
---------

    
`get_title(title, amount, char)`
:   Makes a nice title that is capitalized and centered
    Parameters
    ----------
    title : `string`
        title that has been coded in
    amount : `int`
        how long we make the title
    Returns
    -------
    return : print("invalid values, title length is > graph length")
        returns print if amount is lesser than lenght of title
    return : print(title)
        prints out the title nice and fancy

    
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