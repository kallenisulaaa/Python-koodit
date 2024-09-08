def g_to_l(gallonat):
    litra = gallonat * 3.785
    return litra

def muunna():
    while True:
        maara = float(input("Anna gallonamäärä: \n"))
        if maara < 0:
            break
        litra = g_to_l(maara)
        print(f"{maara} gallonaa on {litra:.2f} litraa")

if __name__ == "__main__":
    muunna()
