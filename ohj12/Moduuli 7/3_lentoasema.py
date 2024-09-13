def main():
    lentoasemat = {}

    while True:
        valinta = input("Valitse toiminto:\n 1: syötä uusi lentoasema \n 2: Hae lentoaseman tiedot \n 3: Lopeta \n")

        if valinta == "1":
            icao = input("Syötä lentoaseman ICAO-koodi: \n")
            nimi = input("Syötä lentoaseman nimi: \n")
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.\n")
        elif valinta == "2":
            icao = input("Anna haettavan lentoaseman ICAO-koodi: \n")
            if icao in lentoasemat:
                print(f"Lentoaseman nimi: {lentoasemat[icao]} \n")
            else:
                print("Lentoasemaa ei löytynyt.\n")
        elif valinta == "3":
            print("Ohjelmaa suljetaan.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.\n")

if __name__ == "__main__":
    main()