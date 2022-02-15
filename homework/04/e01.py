import random

def get_lotto_numbers(amount, min, max):
    lotto_numbers = set()
    while len(lotto_numbers) < amount:
        lotto_numbers.add(random.randint(min,max))
    return lotto_numbers

#def get_lotto_numbers2(amount, min, max):
#    lotto_numbers2 = []
#    for num in range(amount):
#        num = random.randint(min, max)
#        lotto_numbers2.append(num)
#   return lotto_numbers2








print(get_lotto_numbers(7, 1, 40))
#print(get_lotto_numbers2(7, 1, 20))