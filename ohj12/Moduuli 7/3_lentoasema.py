def main():
    lentoasemat = {}

    while True:
        valinta = input("Valitse toiminto:\n 1: syötä uusi lentoasema \n 2: Hae lentoaseman tiedot \n 3: Lopeta")

        if valinta == "1":
            icao = input("Syötä lentoaseman ICAO-koodi: \n")
            nimi = input("Syötä lentoaseman nimi: \n")
            lentoasemat[icao] = nimi
