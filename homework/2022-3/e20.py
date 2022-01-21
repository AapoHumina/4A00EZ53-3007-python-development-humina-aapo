print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
luku = int( input() )
pienin = luku
while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )
    if luku < pienin and luku >= 0:
        pienin = luku

if pienin >= 0:
    print("Pienin antamasi positiivinen luku oli ")
    print(pienin)
else:
    print("Et antanut lukuja.")