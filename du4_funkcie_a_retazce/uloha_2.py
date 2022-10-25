def poc_cislic(retazec):
    pocet = 0
    cisla = "0,1,2,3,4,5,6,7,8,9"
    for i in range(len(retazec)):
        if retazec[i] in cisla:
            pocet +=1
    return pocet
retazec = input("Zadaj retazec: ")
print(poc_cislic(retazec))
