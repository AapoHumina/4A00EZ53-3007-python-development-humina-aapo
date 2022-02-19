import re

def is_date(date):
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
