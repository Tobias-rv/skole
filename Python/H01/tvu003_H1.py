#oppgave 1
import math
def pi(dec = 2):
    if dec > 15:
        print("For mange decimaler")
        print(math.pi)
    else:
        print(round(math.pi, dec))

#oppgave 2
def temperatur(t, g = "C"):
    t = float(t)
    if g == "C":
        t = 1.8 * t + 32
    elif g == "F":
        t = (t - 32) / 1.8
    print(t, g)

#oppgave 3
from time import *
saldo = 500
rentesats = 0.01
endringer = []
x = 0
w = 0
z = 0

def innskud(x):
    global saldo
    global rentesats
    if saldo < 1000000:
        if saldo + x >= 1000000:
            print("Gratulerer, du får bonus renter")
            rentesats = 0.02
    saldo = saldo + x

    endringer.insert(0,"+" + str(x))

def uttak(z):
    global saldo
    global rentesats
    if saldo - z < 0:
        print("Du kan ikke ta ut så mye penger")
    else:
        if saldo > 1000000:
            if saldo - z < 1000000:
                print("Du får normal rente")
                rentesats = 0.01
        saldo = saldo - z

    endringer.insert(0,"-" + str(z))

def beregnRente():
    global saldo
    global rentesats
    y = saldo
    y = y * rentesats
    print(y)

def renteoppgjør():
    global saldo
    global rentesats
    global w
    w = saldo
    w = w * rentesats
    saldo = w + saldo

    endringer.insert(0,"+" + str(w))

def valg():
    global x
    global z
    global w
    global endringer
    tilbake = 1

    while tilbake == 1:
        u = int(input("-----------------\n1 - vis saldo\n2 - innskud\n3 - uttak\n4 - renteoppgjør\n5 - Siste endringer\n-----------------\nVelg handling:"))
        if u == 1:
            print(saldo)
            sleep(2)
        elif u == 2:
            x = input("Beløp:")
            x = float(x)
            innskud(x)
        elif u == 3:
            z = input("Beløp:")
            z = float(z)
            uttak(z)
        elif u == 4:
            renteoppgjør()
        elif u == 5:
            listLengde = len(endringer)
            if listLengde > 3:
                nyEndringer = [endringer[i] for i in(0, 1, 2)]
                print(*nyEndringer, sep="\n")
            else:
                print(*endringer, sep="\n")
            sleep(2)

        tilbake = int(input("-----------------\nVil du tilbake til meny?\n1 - Ja\n2 - Nei\n-----------------\nVelg handling:"))
