a = "hell'o'"
b = 'hell"o"'
c = """hello
        world"""
d = '''hello
        world'''
nimi = "Matti"
paino = 25.345456654

#print(a)
#print(b)
#print(c)
#print(d)

print(len(nimi))
print(f"Hello {nimi}, you have bmi = {paino:.3f}")
print(nimi[0],nimi[4])

nimen_pituus = len(nimi)
print(nimen_pituus)

# capitalize() muuttaa ensimmäisen kirjaimen isoksi
matti = "matti"
print(matti.capitalize())

# casefold() muuuttaa pieniksi kirjaimiksi stringin
iso_matti = "MATTI"
print(iso_matti.casefold())

# center() keskittää stringin keskemmälle defaulttina käyttäen välilyöntiä
opiskelija = "HILLA"
print(opiskelija.center(40))

# encode() palautta salatun version stringistä salaten ö ä å
salaisuus = "Ååpån punäiset stringit jälässa tuntuu kivältä "
print(salaisuus.encode())

# isalpha() palautta True jos kaikki merkit ovat aakkosia
hassu_nimi = "Ståle"
hassu_nimi2 = "L33t"
print(hassu_nimi.isalpha())
print(hassu_nimi2.isalpha())

# islower() palautta True jos kaikki merkit ovat pieniä
pikku_nimi ="lelu"
pikku_nimi2 = "Lelu"
print(pikku_nimi.islower())
print(pikku_nimi2.islower())

# isspace() palautta True jos kaikki merkit ovat välilyöntejä
valilyonti = "     "
ei_valilyonti = " moi"
print(valilyonti.isspace())
print(ei_valilyonti.isspace())

print("give a:", end = " ")
aa = input()

print("give b:", end = " ")
bb = input()

print(f"value {aa} in memory address", id(aa))
print(f"value {bb} in memory address", id(bb))

print("Given strings are same",aa == bb)
print("Memory addresses are same",aa is bb)