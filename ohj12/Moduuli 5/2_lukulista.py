lista = []

while True:
    luku = input("Anna luku: \n")
    if luku == "":
        break
    lista.append(int(luku))

loppu = sorted(lista, reverse=True)[:5]
print(loppu)