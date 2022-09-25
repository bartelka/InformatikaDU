cislo = int(input("Zadaj cislo: "))
pocet = 0
while cislo <= 100:
    print(cislo)
    pocet += 1
    cislo = int(input("Zadaj cislo: "))
print("Pocet nacitanych cisel je ", pocet)
