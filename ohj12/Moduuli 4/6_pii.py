import random

def arvioi_pi(pisteet):
    sisalla = 0


    for _ in range(pisteet):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 < 1:
            sisalla += 1

    piiarvio = 4 * sisalla / pisteet
    return piiarvio

pisteet = int(input("Anna arvottavien pisteiden määrä:\n"))
piin_arvo = arvioi_pi(pisteet)
print(f"Piin likiarvo on noin: {piin_arvo}")

