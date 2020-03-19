#Ser om filene er tomme og lager en list/dictionary om nødvendig
import os
if open("karakterer.txt", "r") is False:
    open("karakterer.txt", "w")
if open("emner.txt", "r") is False:
    open("emner.txt", "w")
x = os.path.getsize("emner.txt")
z = os.path.getsize("karakterer.txt")
if x == 0:
    open("emner.txt", "w").write(str("[]"))
if z == 0:
    open("karakterer.txt", "w").write(str("{}"))

#Henter inn liste og dictionary
Emner = eval(open("emner.txt").readline())
Karakterer = eval(open("karakterer.txt").readline())

#Legger til nytt emne
def nyttEmne(emne):
    emne = emne.upper()
    res = []
    global Emner
    if (emne not in Emner):
        Emner.append(emne)
    Emner.sort()

#Lagrer
def lagreEndringer():
    open("emner.txt", "w").write(str(Emner))
    open("karakterer.txt", "w").write(str(Karakterer))
#meny
a = 1
while a > 0:
    valg = int(input("--------------------\n 1 Emneliste\n 2 Legg til emne\n 3 Sett karakter\n 4 Karaktersnitt\n 5 Avslutt\n 6 Lagre endringer\n--------------------\n Velg en handling fra menyen:"))

    if valg == 1:
        nivå = str(input("Nivå:"))
        if nivå == "":
            nivå = "alle"
        for i in Emner:
            for x, c in enumerate(i):
                if c.isdigit():
                    if i[x] == nivå[0]:
                        print(i)
                        break
        if nivå == "alle":
            print(Emner)

    if valg == 2:
        emne = str(input("Emne:"))
        nyttEmne(emne)

    if valg == 3:

        emne = str(input("Emne:"))
        emne = emne.upper()
        nyttEmne(emne)

        karakter = str(input("Karakter:"))
        karakter = karakter.upper()

        #Gjør at programet er fleksibelt med hva man putter inn som karakter
        if karakter == "A" or karakter == "6":
            karakter = 6
            k = "  A"
        elif karakter == "B" or karakter == "5":
            karakter = 5
            k = "  B"
        elif karakter == "C" or karakter == "4":
            karakter = 4
            k = "  C"
        elif karakter == "D" or karakter == "3":
            karakter = 3
            k = "  D"
        elif karakter == "E" or karakter == "2":
            karakter = 2
            k = "  E"
        elif karakter == "F" or karakter == "1":
            karakter = 1
            k = "  F"

        #Erstatter element i listen "Emner" og erstatter det med likt emne + karakteren
        for i in range(len(Emner)):
            if emne in Emner[i]:
                Emner[i] = emne + k
        Emner = list(set(Emner))
        Emner.sort()
        Karakterer[emne] = karakter

    if valg == 4:
        x = 0
        z = 0
        for key in Karakterer:
            x = x + Karakterer[key]
            z = z + 1
        print(x/z)

    if valg == 5:
        x = str(input("Vil du lagre endringer?[Y/N]:"))
        x = x.upper()
        if x == "Y":
            lagreEndringer()
        a = 0

    if valg == 6:
        lagreEndringer()
