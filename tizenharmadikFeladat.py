def bekeresMuveletekkel():
    osszeadandoSzamok = 0
    legnagyobbSzam = 0
    szam = 1
    szamokMennyisege = 0
    while(szam != 0):
        szam:int = int(input("Kérlek adj meg egy pozitív számot: "))
        osszeadandoSzamok += szam
        if(legnagyobbSzam < szam):
            legnagyobbSzam = szam
        szamokMennyisege += 1
    szamokAtlaga = osszeadandoSzamok / szamokMennyisege
    return osszeadandoSzamok, legnagyobbSzam, szamokAtlaga

def kiiras(osszeadandoSzamok:int, legnagyobbSzam:int, szamokAtlaga):
    print(f"A beírt számok összege {osszeadandoSzamok}, A beírt számokból a legnagyobb: {legnagyobbSzam}, A beírt számok átlaga: {szamokAtlaga}")