def get_first_index(string, character):
    length = len(string)
    string_character = string[0]
    index = 0
    while True:
        if string_character == character:
            return index
        else:
            if index < length-1:
                index = index+1
                string_character =string[index]
            else:
                return -1
index = get_first_index("kalle", "l")
print(index) # 2