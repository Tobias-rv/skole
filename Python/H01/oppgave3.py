saldo = 500
rentesats = 0.01
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

def valg():
    global x
    global z
    global w
    print("-----------------\n1 - vis saldo\n2 - innskud\n3 - uttak\n4 - renteoppgjør\n5 - Siste endringer\n-----------------")
    u = input("Velg handling:")
    u = int(u)
    if u == 1:
        print(saldo)
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
        print("+",x,"\n-",z,"\n+", w)
