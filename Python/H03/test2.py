key = 65
save = {"A":["10"],"B":["2"]}
def flereTrekk():
    global key
    global save
    global ft
    x = 0
    z = []
    while x < 2:
        if save[chr(key)][-1] != "   ":
            z.append(save[chr(key)][-1][0])
        x = x + 1
        key = key + 1
    for i in z:
        if z.count(i) > 1:
            print("J")
import os
x = os.path.getsize("save.txt")
print(x)
test = [ '7', "7", 'Q', '1', '9', 'J']
for i in test:
    if test.count(i) > 1:
        print("hei")
