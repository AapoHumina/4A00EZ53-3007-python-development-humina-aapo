# Kysytään käyttäjältä luku
print("Anna luku")
luku = int(input())

# Lasketaan luvun itseisarvo ja tulostetaan se 
if luku > 0:
    print(luku)
else:
    itseisarvo = luku * -1
    print(itseisarvo)