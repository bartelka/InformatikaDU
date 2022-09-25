koncis = int(input("Zadaj cislo: "))
cisla = list(range(1, koncis+1))
def sucet_n(n):
    vysledok = 0
    for cis in n:
        vysledok += cis
    return vysledok
print("Sucet vsetkych cisel od 1 po", koncis, "je: ",sucet_n(cisla))
