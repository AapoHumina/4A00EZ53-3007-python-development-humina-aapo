import random

# random.randint(0, 5) arpoo luvun 0-5 väliltä
# salainen_luku = random.randint(0, 5)
salainen_luku = random.randint(1, 10)
kayttajan_syote = -1
arvauslaskuri = 0

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (1 - 10)")
    kayttajan_syote = int( input() )
    arvauslaskuri = arvauslaskuri + 1

print("oikein!")
print("Arvasit lukua")
print(arvauslaskuri)
print("kertaa")