#oppgagave 1
from math import *
x = int(input("Radiusen på sirkelen:"))
y = x * x * pi
y = round(y, 3)
print("Arialet til sirkelen er:", y)

#oppgave 2
a = str(input("\nSkriv en settning:"))
b = len(a)
z = 0

#Her gjetter man lengden på setningen helt til man får det rett
c = int(input("Gjett hvor mange bokstaver det er i setningen:"))

while c != b:
    c = int(input("Det er feil prøv igjen:"))

if c == b:
    print("Det er rett")

#oppgave 3
x = str(input("\nSkriv inn et tall:"))

#Henter inn et tilfeldig tall fra 0-9
from random import *
y = str(randint(0, 9))

#Legger det tilfeldige tallet bak det som ble skrevet inn og regner ut
z = x + y
x = int(x)
z = int(z)
y = z / x
y = round(y, 2)

print(z, "/", x, "=", y)
