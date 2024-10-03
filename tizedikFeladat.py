def bekeresCiklussal():
    szoveg = []
    bekeres = ""
    while(bekeres != "@"):
        bekeres:str = str(input("Kérlek adj meg egy betűt, vagy egy számot: "))
        szoveg.append(bekeres)
    return szoveg

def kiiras(szoveg):
    print(szoveg)