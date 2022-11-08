def kodovanie(retazec:str, kod:str)->str:
    novy_retazec = ""
    x = 0
    kd = kod
    for i in range(len(retazec)):
        while len(kd) != len(retazec):
            kd += kod[x]
            x += 1
            if x == (len(kod)-1):
                x = 0
        a = ord(retazec[i])
        b = ord(kd[i])
        vysl = (((a-97)+b)%26)+97
        vysl = chr(vysl)
        novy_retazec += vysl
    return novy_retazec
print(kodovanie("ahoj svet", "kvet"))
