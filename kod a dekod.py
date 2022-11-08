def kodovanie(retazec:str, kod:str)->str:
    novy_retazec = ""
    x = 0
    kodicek = kod
    for i in range(len(retazec)):
        while len(retazec) != len(kodicek):
            kodicek += kod[x]
            x += 1
            if x == (len(kod)-1):
                x = 0
        a = ord(retazec[i])
        b = ord(kodicek[i])
        p = a + b
        p = chr(p)
        novy_retazec += p
    return novy_retazec
print(kodovanie("ahoj svet", "kvet"))
