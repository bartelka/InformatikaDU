print("Zvol si interval <a,b> ")
a = int(input("Cislo a: "))
b = int(input("Cislo b: "))
if a > b:
    a, b = b, a
interval = "<" + str(a) + "," + str(b) + ">"
x = int(input("Napis cislo, o kt. chces zistit ci patri do intervalu: "))
if a <= x <= b:
    print("Cislo", x, "patri do intervalu", interval)
else:
    print("Cislo", x, "nepatri do intervalu", interval)
