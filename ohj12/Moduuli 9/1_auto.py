class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto.rekisteritunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus}")
print(f"Auton tämänhetkinen nopeus: {auto.nopeus}")
print(f"Auton kuljettu matka: {auto.matka}")