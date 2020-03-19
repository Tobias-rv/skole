z = 1
while z > 0:
    from random import *
    x = randint(1, 30)
    print(x*"?")

    y = input("Gjette hvor mange ? det vises på skjermen:\n")
    y = int(y)
    print("Det er ", x == y, "\n")
    if x == y
