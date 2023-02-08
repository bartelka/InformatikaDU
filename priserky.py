import random

monsters = []
dlzka = 5
cage = []

def create_monster()->list:
    temp = []
    for i in range(dlzka):
        temp.append(random.randint(0,10))
    return temp

def iq_test(monster:list)->int:
    return monster.count(1)

def sex(monster1, monster2):
      temp = []
      for i in range(dlzka):
          nahoda = random.randrange(1,101)
          if nahoda > 7:
              # normalny sex
              nahoda = random.randrange(1,101)
              #polka od tatka alebo od mamky
              if nahoda > 50:
                  temp.append(monster1[i])
              else:
                  temp.append(monster2[i])
          else:
              temp.append(random.randrange(0,10))
      return temp

for i in range(10):
    cage.append(create_monster())

def rucna_triedicka(c):
    for i in range( len(c) ,0, -1):
        for j in range(0,i-1):
            if iq_test(c[j]) > iq_test(c[j+1]):
                c[j], c[j + 1] = c[j+1], c[j]
    return c

for j in range(250):
    rucna_triedicka(cage)
    cage = cage[len(cage)//2::]
    for i in range(len(cage)):
        cage.append(sex(cage[random.randrange(0,5)],cage[random.randrange(0,5)]))
    print(cage[::-1])
