kort = ["A ", "K ", "Q ", "J ", "10 ", "9 ", "8 ", "7 "]
hj = "\u2665"
kl = "\u2663"
ru = "\u2666"
sp = "\u2660"
type = [hj, kl, ru, sp]

bunke = []
for t in type:
    for k in kort:
        bunke.append(k + t)
open("save.txt", "w").write(str(bunke))

print(A)
def nyttSpill():
    global save
    save = {"A":["   "], "B":["   "], "C":["   "], "D":["   "], "E":["   "], "F":["   "], "G":["   "], "H":["   "]}
    bunke = ['A ♠', 'K ♠', 'Q ♠', 'J ♠', '10 ♠', '9 ♠', '8 ♠', '7 ♠', 'A ♦', 'K ♦', 'Q ♦', 'J ♦', '10 ♦', '9 ♦', '8 ♦', '7 ♦', 'A ♣', 'K ♣', 'Q ♣', 'J ♣', '10 ♣', '9 ♣', '8 ♣', '7 ♣', 'A ♥', 'K ♥', 'Q ♥', 'J ♥', '10 ♥', '9 ♥', '8 ♥', '7 ♥']
    random.shuffle(bunke)
    key = 65
    x = 0
    for i in bunke:
        save[chr(key)].append(i)
        x = x + 1
        if x == 4:
            key = key + 1
            x = 0

while 2 < 1:
    print("A", "B", "C", "D", "E", "F", "G", "H", sep="     ")
    print(save["A"][-1], save["B"][-1], save["C"][-1], save["D"][-1], save["E"][-1], save["F"][-1], save["G"][-1], save["H"][-1], sep=" | ")
    print(len(save["A"])-1, len(save["B"])-1, len(save["C"])-1, len(save["D"])-1, len(save["E"])-1, len(save["F"])-1, len(save["G"])-1, len(save["H"])-1, sep="     ")
    valg = input("Velg bunker:")
    if save[valg[0]][-1][0] == save[valg[1]][-1][0]:
        save[valg[0]].pop()
        save[valg[1]].pop()
