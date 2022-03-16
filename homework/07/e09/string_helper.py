""" 
Module that has function that converts database string to a 2D list.
"""
from logging import raiseExceptions


def csv_to_list(csv):
    """ 
    Converts database string to a 2D list.
    If it can't, raises exception

    Parameters
    ----------
    commas : `int`
        number of commas in given string
    name_list : `list`
        base of 2D list that function will return
    name_list_array : `list`
        name list split on /n so every name is in its own list
    list_name : `list`
        part of name_list_array to be saved in returning name_list
    
    Exceptions
    ----------
    - If csv is not a string
    - If csv doesn't have enough commas (it should always have even numbers if commas)

    Returns
    -------
    return : `list`
        returns 2D list of names
    """
    try:
        commas = csv.count(",")
        if (commas%2) == 0:
            name_list= []
            name_list_array=csv.split("\n")
            for i in range(0,len(name_list_array)):
                list_name=name_list_array[i].split(",")
                name_list.append(list_name)
            return name_list
        else:
            raise Exception("Something is missing")
    except:
        raise Exception("Something went wrong")