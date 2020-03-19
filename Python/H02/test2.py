Emner = ["INFO100", "ECO100", "INFO110"]
nivå = "100"
for i in Emner:
    for x, c in enumerate(i):
        if c.isdigit():
            if str(c) == nivå[0]:
                print(i)
                break
