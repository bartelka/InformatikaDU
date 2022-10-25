def hlad_index(n, retazec:str)->str:
    if n >= len(retazec):
        print("zly index")
    else:
        print(retazec[n])
    return ""
n = int(input("Zadaj porad. cislo: "))
retazec = input("Zadaj retazec: ")
print(hlad_index(n, retazec))

