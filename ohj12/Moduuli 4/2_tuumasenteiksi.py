while True:
    tuuma = int(input("Syötä tuumien määrä:\n"))
    sentit = 2.54 * tuuma
    if tuuma <= 0:
        break
    else:
        print(sentit)