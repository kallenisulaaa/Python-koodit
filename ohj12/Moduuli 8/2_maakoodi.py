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

kursori = yhteys.cursor()
kysely = input("Anna maakoodi: ")
kursori.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type",(kysely,))
tulokset = kursori.fetchall()

for tulos in tulokset:
    print(f"{tulos[0]}: {tulos[1]} kappaletta")

yhteys.close()