# Kysytään käyttäjältä  luku
print("Anna luku")
luku = int(input())

# Tulostetaan n - 0 
i = 0
if luku > 0:
    while i <= luku:
        print(luku)
        luku = luku - 1
elif luku < 0:
    while i >= luku:
        print(luku)
        luku = luku +1
else:
    print(luku)