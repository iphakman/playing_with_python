import random

L = []
R = []


def agregar1():
    g = random.randint(1, 9)
    L.append(g)


def adivina():
    j = input("insert number: ")
    R.append(int(j))


agregar1()

total = 0
cnt = 0

guess = 0

while guess == 0:
    for a in L:
        print("{}".format(a))

    cuenta = len(L)

    circulo = 0

    while circulo < cuenta:
        adivina()


        if R[circulo] == L[circulo]:
            total += 1
        else:
            guess = 1
            circulo = cuenta

        circulo += 1

    del R
    R = []
    agregar1()


print("Tu score is: {}".format(total))
for a in L:
    print("{}".format(a))
