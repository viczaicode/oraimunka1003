def bekeresOsszeadassal():
    osszeadandoSzamok = 0
    szam = 0
    while(szam <= 10):
        szam:int = int(input("Kérlek adj meg egy pozitív számot: "))
        osszeadandoSzamok += szam
    return osszeadandoSzamok

def kiiras(osszeadandoSzamok):
    print(f"A beírt számok összege: {osszeadandoSzamok}")