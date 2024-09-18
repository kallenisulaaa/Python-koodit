import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database= 'flight_game',
    user='kalle',
    password='kalle',
    autocommit=True,
    collation='utf8mb4_general_ci',
    )

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

def koordinaatit(icao):
    kursori = yhteys.cursor()
    kursori.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao,))
    tulos = kursori.fetchone()
    return tulos

from geopy.distance import geodesic

koordinaatit1 = koordinaatit(icao1)
koordinaatit2 = koordinaatit(icao2)

dist = geodesic(koordinaatit1, koordinaatit2).kilometers
print(f"Lentokenttien välinen etäisyys on {dist:.2f} kilometriä.")
