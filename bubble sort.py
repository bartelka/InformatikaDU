import random
zoznam = []
for i in range(10):
    zoznam.append(random.randrange(0,100))

def bubble_sort(zoznam):
    x = len(zoznam)
    while x > 0:
        for i in range(len(zoznam)-1):
            if zoznam[i] > zoznam[i+1]:
                zoznam[i], zoznam[i+1] = zoznam[i+1], zoznam[i]
        x -= 1
    return zoznam
print(zoznam)
print(bubble_sort(zoznam))
