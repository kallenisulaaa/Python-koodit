user = "python"
passwd = "rules"
att = 0

while True:
    usryritys = input("Anna käyttäjätunnus:\n")
    pssyritys = input("Anna salasana:\n")
    att += 1
    if att == 5:
        print("Pääsy evätty.")
        break
    elif usryritys == user and pssyritys == passwd:
        print("Tervetuloa")
        break