x = int(input("Cislo, z ktoreho chces spravit prevatenu hodnotu: "))
if x == 0:
    print("Prevratena hodnota cisla 0 neexistuje.")
else:
    prevratena_hodnota = 1/x
    prevratena_hodnota = round(prevratena_hodnota,2)
    print("Prevratena hodnota cisla " ,x," je ",prevratena_hodnota)
