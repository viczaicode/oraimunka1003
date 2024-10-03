def csakPozitivBekeres():
    szam = 0
    while(szam <= 0):
        szam:int = int(input("Kérlek adj meg egy pozitív számot: "))
    return szam

def kiiras(szam:int):
    print(f"A beírt pozitív számmod: {szam}") 