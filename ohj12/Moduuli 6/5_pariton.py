def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

if __name__ == "__main__":
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = poista_parittomat(luvut)

    print(f"Alkuperäinen lista: \n {luvut}")
    print(f"Karsittu lista: \n {karsittu}")
