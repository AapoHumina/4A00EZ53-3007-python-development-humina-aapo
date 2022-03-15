import re

def is_name(name):
    try:
        name_truth =re.search("^[A-ZÖÄÅ|a-zöäå][A-ZÖÄÅ|a-zöäå]+$", name)
        returning_boolean = bool(name_truth)
        return returning_boolean
    except:
        return False