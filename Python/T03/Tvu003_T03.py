
#Oppgave 1a

#Første utrykket blir false og det andre blir true

#Oppgave 1b

#x != 7 and y <=50
#not(x==7 or y>50)
#blir til
#(x>7 or 50<y) and (x>y or y<100)
#x>7 or (50<y and y<100)

#Oppgave 2
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

#Oppgave 3

x = int(input("tall:"))
if x > 5 and x < 10:
    print("6,7,8 eller 9")
elif x>=10:
    print("minst 10")
elif x<=5 :
    print("max 5")
