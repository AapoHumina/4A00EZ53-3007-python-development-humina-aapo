# Kysytään käyttäjältä luku1
print("Anna luku 1")
luku1 = int(input())

# Kysytään käyttäjältä luku2
print("Anna luku 2")
luku2 = int(input())

# Lasketaan lukujen summa
summa = luku1 + luku2

# Tulostetaan summan mukaan eri asioita 
if summa > 10:
    print("yli 10")
elif summa < 10:
    print("alle 10")
elif summa == 10:
    print("tasan 10")