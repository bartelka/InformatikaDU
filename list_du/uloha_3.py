def sucin(zoznam):
    sucin = 1
    for i in range(len(zoznam)):
        sucin *= zoznam[i]
    return sucin
zoznam = list(range(1, 11))
print(sucin(zoznam))
