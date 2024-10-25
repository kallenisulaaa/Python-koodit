class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def siirry_kerrokseen(self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print("Kerrosta ei ole olemassa.")
            return
        while kohde > self.nykyinen:
            self.kerros_ylos()
        while kohde < self.nykyinen:
            self.kerros_alas()

    def kerros_ylos(self):
        self.nykyinen = self.nykyinen + 1
        print(f"Nykyinen kerros: {self.nykyinen}")

    def kerros_alas(self):
        self.nykyinen = self.nykyinen - 1
        print(f"Nykyinen kerros: {self.nykyinen}")