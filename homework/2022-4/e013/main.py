def calculate_sum(num1, num2):
    sum = num1 +num2
    return sum

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

sum = calculate_sum(6,4)
print(sum)

print(palauta_isoin(1,2,3))