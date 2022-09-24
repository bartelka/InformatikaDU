koncis = int(input("Zadaj prirodz.cislo: "))
cisla = list(range(1, koncis+1))
def delenie_4a7(n):
    for x in n:
        pod1 = x % 7
        pod2 = x % 4
        if pod1 == 0 and pod2 ==0:
            print(x)
    return ""
print("Cisla delitelne 4 a 7 od 1 po N su: ")
print(delenie_4a7(cisla))
