def bekeres():
    szam = int(input("Kérlek adj meg egy számot: "))
    return szam

def osztokSzamolasa(szam:int):
    osztok = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            osztok += i
    return osztok

def kiiras(osztok:int, szam:int):
    if(szam*2 == osztok):
        print(f"A megadott szám egy tökéletes szám. Az összes osztóinak összege: {osztok}")
    else:
        print(f"A megadott szám nem tökéletes!")