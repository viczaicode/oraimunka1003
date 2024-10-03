def bekeresPrim():
    szam=0
    while(szam % 2 == 0):
        szam:int = int(input("Kérlek adj meg egy egész számot: "))
        return szam
    
def primfelbontas(szam:int):
    eredetiSzam = szam
    while(szam % 2 == 0):
        szam /= 2
    return szam, eredetiSzam

def szorzoraBontas(szam:int, eredetiSzam:int):
    szamlalo = 0
    szam = int(szam)
    hanyszorKetto = eredetiSzam/szam
    hanyszorKetto = int(hanyszorKetto)
    #print(szam, eredetiSzam/szam)
    while(hanyszorKetto % 2 == 0):
        hanyszorKetto /= 2
        szamlalo += 1
    print(szamlalo * ("2*") + str(szam))