import random

def noppa(tahko):
    return random.randint(1,tahko)

def pa():
    tahko = int(input("Anna nopan tahkojen määrä:\n"))
    maksimi = tahko
    silm = 0
    while silm != maksimi:
        silm = noppa(tahko)
        print(f"Heiton tulos: {silm}")


if __name__ == '__main__':
    pa()