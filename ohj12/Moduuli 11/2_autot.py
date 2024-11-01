from auto import *

ec = Sähköauto("ABC-15", 180, 52.5)
pm = Polttomoottoriauto("ACD-123", 165, 32.3)

ec.kiihdyta(150)
pm.kiihdyta(120)

ec.kulje(3)
pm.kulje(3)

print(f"{ec.rekisteritunnus} matkamittarilukema: {ec.matka} km")
print(f"{pm.rekisteritunnus} matkamittarilukema: {pm.matka} km")
