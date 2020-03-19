from random import *
def tilfeldig3():
    a = randint(1, 9)
    b = randint(1, 9)
    c = randint(1, 9)
    d = (a, b, c)
    d = sorted(d)
    d = "".join(str(f)for f in d)
    print(d)
