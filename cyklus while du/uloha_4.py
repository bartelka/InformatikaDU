cislo = int(input("Zadaj cele cislo: "))
sucet = cislo
pocet = 1
while cislo != 0:
    cislo = int(input("Zadaj dalsie cele cislo: "))
    pocet += 1
    sucet += cislo
priemer = sucet / (pocet-1)
priemer = round(priemer, 2)
print(priemer)
