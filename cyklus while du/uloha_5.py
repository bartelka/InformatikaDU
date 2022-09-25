slovo = input("Zadaj slovo: ")
pocet_znak = 0
while slovo[0] != "x":
    print(slovo)
    dlzka = len(slovo)
    pocet_znak += dlzka
    slovo = input("Zadaj dalsie slovo: ")
print("Pocet znakov vsetkych slov je ", pocet_znak)
