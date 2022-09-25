sucet = 0
pocet = 0
cislo = int(input("Zadaj cislo: "))
while (sucet + cislo) <= 100:
    pocet += 1
    print(cislo)
    sucet += cislo
    cislo = int(input("Zadaj dalsie cislo: "))
print("Pocet cisel je ", pocet, "a ich sucet je ", sucet)
