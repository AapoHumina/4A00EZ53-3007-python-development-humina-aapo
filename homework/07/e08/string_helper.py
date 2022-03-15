from logging import raiseExceptions


def csv_to_list(csv):
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