lei = float(input("Kuinka monta leiviskää? \n"))
nau = float(input("Kuinka monta naulaa? \n"))
luo = float(input("Kuinka monta luotia? \n"))

nau += lei*20
luo += nau*32
grammat = luo*13.3

kokonaisgrammat = grammat
kilogrammat = int(kokonaisgrammat//1000)
loputgrammat = kokonaisgrammat % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {loputgrammat:.2f} grammaa.")