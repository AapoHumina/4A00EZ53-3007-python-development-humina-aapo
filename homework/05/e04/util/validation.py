import re
"""  
Module that contains functions for 
asking if date is valid date,
asking if email is valid email and
asking if personal ID is valid personal ID
"""
def is_date(date):
    """ 
    is_date function checks if given string is proper date
    in YYYY-MM-DD form, if it is ok return True, else return False
    Parameters
    ----------
    date : `string`
        user given name date, excepting string 
    year_month_day : `list`
        list of strings split on - character from date string
    year : `match object`
        match object representing if the string in list is a proper date
    month : `match object`
        match object representing if the string in list is a proper date
    day : `match object`
        match object representing if the string in list is a proper date
    
    Exceptions
    ----------
    - If given date cannot be run, returns False

    Returns
    -------
    Returns True if date is proper date, else returns False
    """
    try:
        if date.startswith("-") or date.endswith("-"):
            return False
        year_month_day = re.split("-", date)
        year = re.search("^[0-9]{4}$", year_month_day[0])              #searches if number is in range of 0000-9999
        month = re.search("^0[1-9]|1[0-2]$", year_month_day[1])        #searches if number is in range of 01-09 or 10-12
        day = re.search("^0[1-9]|[12][0-9]|3[01]$", year_month_day[2]) #searches if number is in range of 01-09 or 10-29 or 30-31 

        if bool(year) == True and bool(month) == True and bool(day) == True:
            return True
        else:
            return False
    except:
        return False

# A valid email address consists of an email prefix and an email domain, both in acceptable formats.
# The prefix appears to the left of the @ symbol.
# The domain appears to the right of the @ symbol.
# For example, in the address example@mail.com, "example" is the email prefix, and "mail.com" is the email domain.
# Acceptable email prefix formats
#   Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
#   An underscore, period, or dash must be followed by one or more letter or number.
# Acceptable email domain formats
#   Allowed characters: letters, numbers, dashes.
#   The last portion of the domain must be at least two characters, for example: .com, .org, .cc
#   Domain names are only allowed to be 63 characters in length
# Does upper case matter in email address?
#    No. Email addresses are not case sensitive. 
#    Having letters in all lowercase makes the email address easier to read, 
#    but the oversight won't stop your messages from being delivered.


def is_email(email):
    """ 
    is_email function checks if given string is proper email
    in jussi.pohjolainen@tuni.fi form, if it is ok return True, else return False
    Parameters
    ----------
    email : `string`
        user given email, excepting string 
    email_parts : `list`
        list of strings split on @ character from email string
    email_prefix : `string`
        prefix part of email, split from email at @ char
    email_domain : `string`
        domain part of email, split from email at @ char
    x : `match object`
        match object that searches for any illegal chars in email_prefix
    y : `match object`
        match object that searches for any illegal chars in email_domain
    i : `list`
        list that is used to check if illegal . - _ placements occur in email_prefix
    j : `list`
        list that is used to check if illegal . - placements occur in email_domain
    email_domain_list : `list`
        list split from email_domain, used to check if last part of domain is proper length
    
    Exceptions
    ----------
    - If given email cannot be run, returns False

    Returns
    -------
    Returns True if email is proper email, else returns False
    """
    try:
        if len(email) > 254 or len(email) < 6:                              # If email is too long or short return False
            print("Given email is too long or short")
            return False
        email = email.lower()                                               # Emails are not case sensitive
        email_parts = re.split("@", email, 1)
        email_prefix = email_parts[0]
        email_domain = email_parts[1]
        x = re.search("[^a-zöäå0-9._-]", email_prefix)                      # Search for any not allowed characters
        y = re.search("[^a-zöäå0-9.-]", email_domain)                       # -//-
        i = re.findall("^[.]|[.]$|^-|-$|^_|_$|[.\-_][.\-_]", email_prefix)  # Searching if email prefix or domain has any . - _ characters
        j = re.findall("^[.]|[.]$|^-|-$|[.-][.-]", email_domain)            # with no letters before or after it
        if bool(x) or bool(y) or bool(i) or bool(j):
            print("There are illegal characters in your email or invalid . - _ characters")
            return False
        if email_domain.count(".") < 1:                                     # If there is not a single dot in domain name, return False
            print("Emails domain name should usually have at least one dot")
            return False
        email_domain_list = re.split("[.]", email_domain)                   
        if len(email_domain_list[len(email_domain_list)-1]) < 2:            # Checking that last portion of domain name is at least 2 characters
            print("Last portion of domain name too short")
            return False
        return True
    except:
        print("Given email was not proper email")
        return False

# Personal ID is 11 characters long and is in form DDMMYYXNNNT 
# DDMMYY is persons birthdate example 080793
# X is mark when person was born
#   1800: +
#   1900: -
#   2000: A
# NNN is invidual number to differentiate between people born in same date. 
#   For women the mumber is even, for men odd.
#   Number for official invidual numbers is between 002-889
# T is a checking number
#   It is got by diving the PPKKVVNNN number by 31 and keeping the remainder.
#   The number (that is between 0-30) is then converted to a character by a table.  
# 0	    0	16	H
# 1	    1	17	J
# 2	    2	18	K
# 3	    3	19	L
# 4	    4	20	M
# 5	    5	21	N
# 6	    6	22	P
# 7	    7	23	R
# 8	    8	24	S
# 9	    9	25	T
# 10	A	26	U
# 11	B	27	V
# 12	C	28	W
# 13	D	29	X
# 14	E	30	Y
# 15	F

def is_personal_id(id):
    """ 
    is_personal_id function checks if given string is proper ID
    in DDMMYYXNNNT form, if it is ok return True, else return False
    Parameters
    ----------
    id : `string`
        user given id, excepting string 
    id_true : `match object`
        match object that searches for any illegal chars in ID
    id_bdate : `string`
        date part of ID, split from ID at - or A or + char
    id_invid_num : `string`
        invidual number part of ID, split from ID at - or A or + char
    id_invid_num_true : `match object`
        match object that searches if invidual number is proper ID number 
    id_bdate_true : `match object`
        match object that searches if date part of ID is valid date
    check : `int`
        safety number for checking that ID is valid
    check_chars: `string`
        char string for checking if safety numbers match
    
    Exceptions
    ----------
    - If given ID cannot be run, returns False

    Returns
    -------
    Returns True if ID is proper ID, else returns False
    """
    try:    
        if len(id) != 11:                                                                                       # Checking if ID is too short or long, id is always 11 char long
            print("ID wrong length")
            return False
        id_true =  re.search("[^A-FHJ-NPR-YA0-9+-]", id)                                                        # Search for illegal characters in ID
        if bool(id_true):
            print("Not a proper ID for there are illegal characters")
            return False
        id_list = re.split("[+A-]", id, 1)
        id_bdate = id_list[0]
        id_invid_num = id_list[1]
        if len(id_bdate) != 6 or len(id_invid_num) != 4:                                                        # Because ID is always 11 char long, parts are fixed length too
            print("Not a proper ID for the year mark was in the wrong spot")
            return False
        id_invid_num_true = re.search("^(00[2-9]|0[1-9][0-9]|[1-8][0-9][0-9])[0-9A-FHJ-NPR-Y]$", id_invid_num)  # Search invidual number, first 002-009, 010-099, 100-899
        id_bdate_true = re.search("^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])([0-9][0-9])$", id_bdate)            # Search date DD between 01-09,10-29,30-31
        if  bool(id_bdate_true) == False or bool(id_invid_num_true) == False:                                   # MM between01-09,10-12 YY between 00-99
            print("Not a proper birthdate or it is in wrong order, correct order DDMMYY")
            return False
        check = int(id_bdate + id_invid_num[0] + id_invid_num[1] +id_invid_num[2])%31                           # Calculating remainder for check character in the IDs end
        check_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        if check_chars[check] != id_invid_num[3]:                                                               # Checking if safety character matches table
            print("Your ID is not valid")
            return False
        return True
    except:
        print("You did not give ID")
        return False