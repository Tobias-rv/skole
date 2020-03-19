x = input("Skriv inn et tall:\n")
z = input("Skriv inn et tall som er likt eller høyere:\n")
z = int(z)
x = int(x)
y = 0
while z > x:
    y = y + x
    x = x + 1
print (y+z)
