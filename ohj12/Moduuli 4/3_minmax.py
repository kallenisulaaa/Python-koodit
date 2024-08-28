pienin = None
suurin = None

while True:
    syote = input("Syötä luku, tai tyhjä lopettaaksesi:\n")
    if syote == "":
        break
    luku = int(syote)
    if pienin == None or luku < pienin:
        pienin = luku
    if suurin == None or luku > suurin:
        suurin = luku
print("Pienin luku:\n",pienin)
print("Suurin luku:\n",suurin)