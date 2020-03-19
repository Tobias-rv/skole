list = {"k":1, "f":2}

with open("emner.txt", "w") as file:
    file.write(str(list))

with open("emner.txt", "r") as file:
    list2 = eval(file.readline())
file.close()
print(list, type(list), type(list["k"]))
print(list2, type(list), type(list2["k"]))
