#!/bin/python3

print("Anna neliön korkeus")
korkeus = int( input())
print("Anna neliön leveys")
rivi = int( input())

i = 0
j = 0
while j < korkeus:

  i = 0
  while i < rivi:
    # Tulosta "X" ilman enter painallusta
    # Huom! tämä vaatii python3 - tulkin joka asetettu päälle rivillä 1
    print("X", end='')
    i = i + 1
  
  # Tulosta enter
  print()
  j = j + 1