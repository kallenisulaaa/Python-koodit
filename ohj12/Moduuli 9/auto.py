import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
auto = Auto("ABC-123", 142)

def luo_autot(maara):
    autot = []
    for i in range(1, maara + 1):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))
    return autot

def tulosta_autot(autot):
    print(f"{'Rekisteritunnus':<12}{'Huippunopeus':<13}{'Nopeus': <8}{'Matka': <6}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<13}{auto.nopeus:<8}{auto.matka:<6}")