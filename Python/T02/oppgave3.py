x = input("Skriv inn et tall:")

from random import *
y = randint(0, 9)
y = str(y)

z = x + y
z = int(z)
x = int(x)
y = z / x
y = round(y, 2)

print(z, "/", x, "=", y)
