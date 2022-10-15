def obdlznik(sirka:int, znak:str):
        print(znak * sirka)
        print(znak + " "*(sirka-2) + znak)
        print(znak * sirka)

sirka = int(input("Zadaj sirku obdlznika: "))
znak  = input("Zadaj znak: ")
print(obdlznik(sirka, znak))
