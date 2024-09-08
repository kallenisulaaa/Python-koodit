import math

def yksikko(halk, hinta):
    sade = halk / 2 / 100
    pinta_ala = math.pi * (sade ** 2)
    yksikko = hinta / pinta_ala
    return yksikko

if __name__ == '__main__':
    halk1 = float(input('Anna ensimmäisen pizzan halkaisija (cm): \n'))
    hinta1 = float(input('Anna ensimmäisen pizzan hinta (euroa): \n'))
    halk2 = float(input('Anna toisen pizzan halkaisija (cm): \n'))
    hinta2 = float(input('Anna toisen pizzan hinta (euroa): \n'))
    yksikkoh1 = yksikko(halk1, hinta1)
    yksikkoh2 = yksikko(halk2, hinta2)

    print(f'Ensimmäisen pizzan yksikköhinta on {yksikkoh1:.2f} €/m²')
    print(f'Toisen pizzan yksikköhinta on {yksikkoh2:.2f} €/m²')
    if yksikkoh1 < yksikkoh2:
        print('Ensimmäinen pizza antaa paremman vastineen rahalle.')
    else:
        print('Toinen pizza antaa paremman vastineen rahalle.')