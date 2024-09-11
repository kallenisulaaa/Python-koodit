kk = {
    1: "talvi", 2: "talvi", 3: "kevät",
    4: "kevät", 5: "kevät", 6: "kesä",
    7: "kesä", 8: "kesä", 9: "syksy",
    10: "syksy", 11: "syksy", 12: "talvi"
}
numero = int(input("Syötä numero (1-12):\n"))
if 1 <= numero <= 12:
    va = kk[numero]
    print(f"Kuukausi {numero} kuuluu vuodenaikaan {va}.")
else:
    print("Virheellinen numero, syötä numero väliltä 1-12.")