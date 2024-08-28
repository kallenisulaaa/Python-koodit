pituus = int(input("Anna kuhan pituus:\n"))

if pituus >= 37:
    print("Hyvä saalis!")
if pituus < 37:
    print("Laske kala takaisin järveen! Saaliisi on", 37 - pituus,"cm alle sallitusta pyyntimitasti.")
