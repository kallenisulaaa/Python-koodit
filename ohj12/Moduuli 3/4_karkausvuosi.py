vuosi = int(input("Anna vuosi:\n"))

if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print("Annettu vuosi on karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi.")