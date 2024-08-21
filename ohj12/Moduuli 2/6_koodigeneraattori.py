import random

kolme = ""
for _ in range(3):
    kolme += str(random.randint(0,9))
nelja = ""
for _ in range(4):
    nelja += str(random.randint(1,6))
print(kolme)
print(nelja)