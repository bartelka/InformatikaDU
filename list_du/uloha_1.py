def vypis_typy(zoznam):
    for i in range(len(zoznam)):
        znak = zoznam[i]
        if type(znak) == str:
            print(znak,"- retazec")
        elif type(znak) == int or type(znak) == float:
            print(znak, "- cislo")
        else:
            print(znak, "- iny typ")

zoznam = [12, 'x', None, 3.14, [], range(5), '123']
print(vypis_typy(zoznam))
