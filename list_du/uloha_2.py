def nakup(zoznam):
    cena = 0
    for i in range(len(zoznam)):
        if i % 2 != 0:
            cena += zoznam[i] * zoznam[i-1]
    return cena
zoznam = [3, 2.5, 0.5, 10, 1.2, 1.2]
print(nakup(zoznam))
