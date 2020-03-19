a = int(input("Oppgi alder:\n"))

b = int(input("Hvor lenge har du bodd i Tulleby:\n"))

if a >= 30 and b >= 9:
    print("Du kan bli ordfører eller sitte i bystyret")

elif (a < 30 and b < 9) and (a >= 25 and b >= 5):
    print("Du kan sitte i bystyret \nPrøv igjen om",30 - a, "år for å blir ordfører")

elif a < 25:
    print("Du er ikke kvalifisert enda, prøv igjen om", 25 - a, "år")

elif b < 5:
    print("Du er ikke kvalifisert enda, prøv igjen om", 5 - b, "år")
