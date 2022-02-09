#!/bin/python3

print("Anna neliön korkeus")
korkeus = int( input() )
rivi = 0
while rivi < korkeus:
  
  sarake = 0
  while sarake < korkeus:
    # Tulosta " " ilman enter painallusta
    # Huom! tämä vaatii python3 - tulkin joka asetettu päälle rivillä 1
    if sarake == rivi:
        print("X", end='')
        sarake = sarake + 1
    else:
        print(" ", end='')
        sarake = sarake + 1
  
  # Tulosta enter
  print()
  rivi = rivi + 1