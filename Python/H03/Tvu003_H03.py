import random
import os
key = 65
visuelt = []
k = 1
if os.path.isfile("save.txt") == False:
    open("save.txt", "w")
def nyttSpill():
    global save
    global key
    save = {"A":["   "], "B":["   "], "C":["   "], "D":["   "], "E":["   "], "F":["   "], "G":["   "], "H":["   "]}
    bunke = ['A s', 'K s', 'Q s', 'J s', '10 s', '9 s', '8 s', '7 s', 'A r', 'K r', 'Q r', 'J r', '10 r', '9 r', '8 r', '7 r', 'A k', 'K k', 'Q k', 'J k', '10 k', '9 k', '8 k', '7 k', 'A h', 'K h', 'Q h', 'J h', '10 h', '9 h', '8 h', '7 h']
    random.shuffle(bunke)
    x = 0
    key = 65
    for i in bunke:
        save[chr(key)].append(i)
        x = x + 1
        if x == 4:
            key = key + 1
            x = 0
def flereTrekk():
    global key
    global save
    ft = 0
    x = 0
    z = []
    key = 65
    while x < 8:
        if save[chr(key)][-1] != "   ":
            z.append(save[chr(key)][-1][0])
        x = x + 1
        key = key + 1
    for i in z:
        if z.count(i) > 1:
            ft = ft + 1
    if ft > 0:
        valg = input("Velg bunker:")
        valg = valg.upper()
        if (save[valg[0]][-1] or save[valg[1]][-1]) != "   ":
            if save[valg[0]][-1][0] == save[valg[1]][-1][0]:
                save[valg[0]].pop()
                save[valg[1]].pop()
    else:
        input("Ingen flere trekk. Trykk enter for å fortsette:")
        nyttSpill()
def nyttKort():
    global visuelt
    global save
    symboler = {"s":"\u2660", "r":"\u2666", "k":"\u2663", "h":"\u2665"}
    visuelt = []
    for i in save:
        if save[i][-1] != "   ":
            visuelt.append(save[i][-1][0:2] + " " + symboler[save[i][-1][-1]])
        else:
            visuelt.append("    ")
def printing():
    global save
    global visuelt
    print("A", "B", "C", "D", "E", "F", "G", "H", sep="      ")
    print(*visuelt, sep=" | ")
    print(len(save["A"])-1, len(save["B"])-1, len(save["C"])-1, len(save["D"])-1, len(save["E"])-1, len(save["F"])-1, len(save["G"])-1, len(save["H"])-1, sep="      ")
x = os.path.getsize("save.txt")
if x < 5:
    open("save.txt", "w").write("{}")
    nyttSpill()
else:
    save = eval(open("save.txt").readline())
while 0 < 1:
    nyttKort()
    printing()
    flereTrekk()
    open("save.txt", "w").write(str(save))
