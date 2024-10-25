from hissi import Hissi

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissien_lkm = lkm
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(self.alin, self.ylin))

    def aja_hissia(self, numero, kohde):
        if numero > len(self.hissit) or numero < 1:
            print("Hissiä ei ole.")
        else:
            self.hissit[numero - 1].siirry_kerrokseen(kohde)