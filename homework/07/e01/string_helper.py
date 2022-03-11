from logging import raiseExceptions


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

print(csv_to_list("1,Jussi,Virtanen\n2,Pekka,Keinänen"))