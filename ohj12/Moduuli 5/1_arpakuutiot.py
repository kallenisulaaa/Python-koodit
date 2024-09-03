import random

arpa = int(input("Kuinka monta noppaa?\n"))

summa = 0

for(i)in range(arpa):
    heitto = random.randint(1,6)
    summa += heitto

print(f"Noppien silmälukujen summa on {summa}")