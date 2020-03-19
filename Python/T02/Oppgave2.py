a = input("Skriv en settning (kun a-z);\n")
b = len(a)
z = 0

while z < 1:

    c = input("\nGjett hvor mange bokstaver det er i setningen:\n")
    c = int(c)

    if c == b:
        print("Det er rett")
        z = z + 1
    elif c != b:
        print("Det er feil")
