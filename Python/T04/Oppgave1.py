def fak1(x):
    z = x
    while x > 1:
        x = x - 1
        z = z * x
    return z

def fak2(a):
    e = 1
    for b in range(a):
        c = b + 1
        e = e * c
    return e
