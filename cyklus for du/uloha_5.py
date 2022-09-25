koncis = int(input("Zadaj cislo: "))
cisla = list(range(1, koncis+1))
def scitanie_cisel(n):
    pocet = 0
    for i in n:
        if i % 2 ==0:
            pocet +=1
    return pocet
print("Pocet parnych cisel od 1 po", koncis, "je ", scitanie_cisel(cisla))
