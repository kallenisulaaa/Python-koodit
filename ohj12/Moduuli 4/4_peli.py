import random

luku = random.randint(1,10)
arvaus = 0
while True:
    arvaus = int(input("Arvaa luku:\n"))
    if arvaus == luku:
        print("Oikein")
        break
    elif luku > arvaus:
        print("Liian pieni arvaus")
    elif luku < arvaus:
        print("Liian suuri arvaus")