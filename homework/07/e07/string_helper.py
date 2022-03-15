
def csv_to_list(csv):
    try:
        name_list= []
        name_list_array=csv.split("\n")
        for i in range(0,len(name_list_array)):
            list_name=name_list_array[i].split(",")
            name_list.append(list_name)
        return name_list
    except:
        raise Exception("Something went wrong")