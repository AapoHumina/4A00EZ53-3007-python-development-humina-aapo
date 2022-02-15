import random

def get_lotto_numbers(min = 1, max = 40, amount = 7):
    if min >= max or amount > max or amount < 0:
        raise Exception ("invalid numbers")
    lotto_numbers = set()
    while len(lotto_numbers) < amount:
        lotto_numbers.add(random.randint(min,max))
    return lotto_numbers








print(get_lotto_numbers(1, 40, 7))
print(get_lotto_numbers(min = 1, max = 40, amount = 7))
#print(get_lotto_numbers(1, 50))
#print(get_lotto_numbers(1, 40))
print(get_lotto_numbers())
print(get_lotto_numbers(1, 10, 4))
print(get_lotto_numbers(1, 6, 6))
print(get_lotto_numbers(1, 6, 7))