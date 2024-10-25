import random
from auto import luo_autot
from auto import tulosta_autot


autot = luo_autot(10)
kilpailu = True
while kilpailu:
    for auto in autot:
        auto.kiihdyta(random.randint(-10,15))
        auto.kulje(1)
        if auto.matka > 10000:
            kilpailu = False
            break

tulosta_autot(autot)