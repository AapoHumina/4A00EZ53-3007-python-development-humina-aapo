# Funktio joka printtaa nimen
def my_name():
    print("Aapo")

# Funktio joka palauttaa nimen
def my_name_return():
    return "Aapo"

# Funktio joka printtaa annettua stringia n kertaa
def output(sana, kerroin):
    print(sana * kerroin)

# Funktio saa 3 argumenttia ja palauttaa niistä isoimman
def palauta_isoin(i, j, k):
    if i > j and i > k:
        return i
    elif j > i and j > k:
        return j
    elif k > j and k > i:
        return k
    else:
        return i


my_name()
print(my_name_return())
output("hello", 2)
print(palauta_isoin(1,2,3))
