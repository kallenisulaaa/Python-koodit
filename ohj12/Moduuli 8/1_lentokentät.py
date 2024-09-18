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

def hae(icao):
    kursori = yhteys.cursor()
    kursori.execute("SELECT name, municipality FROM airport WHERE ident = %s",(icao,))
    tulos = kursori.fetchone()
    yhteys.close()
    if tulos:
        return tulos
    else:
        return None
def main():
    icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
    lentokentta = hae(icao)

    if lentokentta:
        nimi, kunta = lentokentta
        print(f"Lentokenttä: {nimi}, Sijaintikunta: {kunta}")
    else:
        print("Lentokenttää ei löytynyt ICAO-koodilla.")


if __name__ == '__main__':
    try:
        main()
    finally:
        yhteys.close()