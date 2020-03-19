import math
x = input("Skriv inn et tall:\n")
y = input("Skriv inn enda et tall:\n")
z = x + y
y = y + x

z = float(z)
y = float(y)

w = z * y
w = math.sqrt(w)
w = round(w, 2)
print("Kvadrat roten av", y, "*", z, "=", w)
