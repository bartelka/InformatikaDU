cislo = int(input("Zadaj aspon dvojciferne cislo: "))
posled_cif = cislo%10
predpos_cif =(cislo%100)//10
sucet = posled_cif + predpos_cif
if sucet%2 == 0:
    print("Sucet poslednych dvoch cifier je parny")
else:
     print("Sucet poslednych dvoch cifier je neparny")
