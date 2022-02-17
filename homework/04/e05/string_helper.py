
def is_name(name, ignore_case=False):
    if ignore_case:
        if name.rfind(" ") == -1 or name.count(" ") > 1:
            return False
        else:
            name_list= name.split(" ")
            first_name = name_list[0]
            last_name = name_list[1]
        if first_name.isalpha() == False or last_name.isalpha() == False:
            return False
        elif len(first_name) >= 2 and len(last_name) >= 2:
            return True
    else:
        if name.rfind(" ") == -1 or name.count(" ") > 1:
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

def list_to_str(my_list):
    if len(my_list) == 0:
        return "Empty List"
    print("Database:")
    for index in range(0, len(my_list)):
        print(index+1, my_list[index])