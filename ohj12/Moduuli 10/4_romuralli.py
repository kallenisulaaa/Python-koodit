from auto import *

autot = luo_autot(10)
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tilanne()

kilpailu.tilanne()
print("Kilpailu on päättynyt.")