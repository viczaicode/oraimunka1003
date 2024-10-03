def bekeresGyakorlas():
    szam=0
    while not(szam >= 10 and szam <= 20):
        szam:int = int(input("Kérlek adj meg egy egész számot 10 és 20 között: "))
    return szam

def oszthatoE(szam:int):
    joszamok = []
    while(szam % 2 == 0):
        joszamok.append(szam)
        szam /= 2
    return joszamok

def kiiras(joszamok):
    print(joszamok)
