class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print(f"Nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta(self):
        super().tulosta()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta(self):
        super().tulosta()
        print(f"Päätoimittaja: {self.toimittaja}")