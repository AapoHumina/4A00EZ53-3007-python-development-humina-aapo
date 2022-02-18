import re

"""
def is_date(date):
    
    if not isinstance(date, (str)):
        raise Exception("date should be a string")
    if date.count("-") != 2:
        raise Exception("please use dashes to differentiate between numbers")
    
    try:
        year_month_day = re.split("-", date)
        year = re.search("^[0-9]{4}$", year_month_day[0])
        for i in range(1, 13):
            if i == int(year_month_day[1]):
                month = True
        for i in range(1, 32):
            if i == int(year_month_day[2]):
                day = True
        if bool(year) == True and month == True and day == True:
            return True
        else:
            return False
    except:
        return False
"""

def is_date(date):
    try:
        year_month_day = re.split("-", date)
        year = re.search("^[0-9]{4}$", year_month_day[0])
        month = re.search("^0[1-9]|1[0-2]$", year_month_day[1])
        day = re.search("^0[1-9]|[12][0-9]|3[01]$", year_month_day[2])

        if bool(year) == True and bool(month) == True and bool(day) == True:
            return True
        else:
            return False
    except:
        return False