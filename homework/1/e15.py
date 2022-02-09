# Kysytään käyttäjältä kuukausi
print("Anna kuukausi 1-12")
month = int(input())

# Kysytään käyttäjältä päivä
print("Anna päivä 1-31")
day = int(input())

#Tarkistetaan onko vappu tai itsenäisyyspäivä ja printataan päivää vastaava tulos 
if month == 5 and day == 1:
    print("Nyt on vappu :)")
elif month == 12 and day == 6:
    print("Nyt on itsenäisyyspäivä :)")
elif month < 1 or month > 12 or day < 1 or day > 31:
    print("Annoit fiktiivisen päivämäärän :/")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä :(")