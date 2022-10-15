def priemer(a:int, b:int):
    priem = (a+b)/2
    priem = round(priem, 2)
    return priem

a = int(input("Zadaj cislo a: "))
b = int(input("Zadaj cislo b: "))
print(priemer(a,b))
