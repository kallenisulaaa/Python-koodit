sp = input("Syötä sukupuolesi:\n")
hg = int(input("Syötä hemoglobiiniarvosi (g/l):\n"))
if sp == "Nainen":
    if hg < 117:
        print("Hemoglobiiniarvosi ovat alhaiset.")
    elif hg > 175:
        print("Hemoglobiiniarvosi ovat korkeat.")
    else:
        print("Hemoglobiiniarvosi ovat normaalit.")
if sp == "Mies":
    if hg < 134:
        print("Hemoglobiiniarvosi ovat alhaiset.")
    elif hg > 195:
        print("Hemoglobiiniarvosi ovat korkeat.")
    else:
        print("Hemoglobiiniarvosi ovat normaalit.")