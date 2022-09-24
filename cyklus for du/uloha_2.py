koncis = int(input("Zadaj prirodz.cislo: "))
cisla = list(range(1, koncis+1))

def suc_parcis(n):
    sucet = 0
    for cislo in n:
        podiel = cislo % 2
        if podiel == 0:
           sucet +=cislo
    return sucet
print("Sucet parnych cisel od 1 po N je ", suc_parcis(cisla))
