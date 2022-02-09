# Kysytään käyttäjältä arvosana
while 1 > 0:
    print("Anna arvosanasi 0-5: ", end = "")
    arvosana = input()

# Katsotaan mitä outputtia arvosana vastaa ja annetaan se,
# jos käyttäjä antaa jotain muuta niin kysytään arvosanaa uudelleen
    if arvosana == '0':
        print("Fail")
        break
    elif arvosana == '1' or arvosana == '2':
        print("Weak")
        break
    elif arvosana == '3' or arvosana == '4':
        print("Good")
        break
    elif arvosana == '5':
        print("Excellent")
        break
    else:
        print("Anna arvosana väliltä 0-5")
        continue