koncis = int(input("Zadaj prirodz.cislo n: "))
cisla = list(range(1, koncis+1))
def delenie_3(n):
    for cislo in n:
        podiel = cislo % 3
        if podiel == 0:
            print(cislo)
    return""
print("Cisla delitelne od 1 po N su: ")
print(delenie_3(cisla))
