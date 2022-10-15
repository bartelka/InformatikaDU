def riadok(n:int, text):
    if text != "":
        text = " "+text+" "
    if text == "":
        text = " "+"-"+" "
    zac = (n-len(text))//2
    kon = n-len(text)-zac
    print("*"*zac, text, "*"*kon)

n = int(input("Zadaj n: "))
text = input("Zadaj text: ")
print(riadok(n, text))
