zacinter = int(input("Cislo, kt. bude zacinat tvoj interval: "))
koninter = int(input("Cislo, kt. bude koncit tvoj interval: "))
if zacinter > koninter:
    zacinter, koninter = koninter, zacinter
cisla = list(range(zacinter,koninter))
def pocet_cisel(n):
    pocet = 0
    for x in n:
        if x % 8 == 0:
            pocet += 1
    return pocet
interval = "<" + str(zacinter) + "," + str(koninter) + ">"
print("Pocet cisel delitelnch 8 z tvojho intervalu ", interval, "je", pocet_cisel(cisla))
