# Kysytään käyttäjältä kuukausi
print("Anna kuukausi 1-12")
month = int(input())

# Kysytään käyttäjältä päivä
print("Anna päivä 1-31")
day = int(input())

#Tarkistetaan onko jouluaatto vai ei ja printataan päivää vastaava tulos 
if month == 12 and day == 24:
    print("Hyvää joulua :)")
elif month < 1 or month > 12 or day < 1 or day > 31:
    print("Annoit fiktiivisen päivämäärän :/")
else:
    print("Ei ole vielä jouluaatto :(")