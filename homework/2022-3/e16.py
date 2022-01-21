# Tulostetaan luvut 0-9
i = 0
while i < 10:
    print(i)
    i = i + 1

# Tulostetaan luvut 1-10 
i = 1
while i < 11:
    print(i)
    i = i + 1

# Tulostetaan luvut 10-1
i = 10
while i > 0:
    print(i)
    i = i - 1

# Tulostetaan luvut 1-n kun n kysytään käyttäjältä
print("Anna luku")
luku = int(input())
i = 1
while i < luku+1:
    print(i)
    i = i + 1