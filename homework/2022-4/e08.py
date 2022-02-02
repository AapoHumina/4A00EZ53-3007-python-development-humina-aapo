# Funktio joka printtaa annettua stringia n kertaa
def get_int(question,lowest_number, highest_number):
    while 1 > 0:
        print("Give grade:", end = " ")
        number = input()
        if number == '4':
            return number
        elif number == '5':
            return number    
        elif number == '6':
            return number
        elif number == '7':
            return number
        elif number == '8':
            return number
        elif number == '9':
            return number
        elif number == '10':
            return number
        else:
            print("Grade must be 4-10")
            continue




grade = get_int("Give grade", 4, 10)
print("You gave", grade)