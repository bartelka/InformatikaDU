print("Zadaj strany trojuholnika")
a = int(input("strana a: "))
b = int(input("strana b: "))
c = int(input("strana c: "))
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("Dane hodnoty su stranami rovnostranneho trojuholnika.")
    elif a == b is not c or a == c is not b or b == c is not a:
        print("Dane hodnoty su stranami rovnoramenneho trojuholnika.")
    elif a is not b is not c:
        if c**2 == a**2 + b**2 or a**2 == b**2 +c**2 or b**2 == a**2 +c**2:
            print("Dane hodnoty su stranami roznostranneho trojuholnika, kt. je zaroven pravouhly.")
        else:
            print("Dane hodnoty su stranami roznostranneho trojuholnika.")
else:
    print("Dane hodnoty nie su stranami trojuholnika.")
