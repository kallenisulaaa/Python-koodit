import random

def noppa():
    return random.randint(1,6)

def pa():
    silm = 0
    while silm != 6:
        silm = noppa()
        print(f"Heiton tulos: {silm}")


if __name__ == '__main__':
    pa()