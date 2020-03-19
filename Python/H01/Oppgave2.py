def temperatur(t, g = "C"):
    t = float(t)
    if g == "C":
        t = 1.8 * t + 32
    elif g == "F":
        t = (t - 32) / 1.8 
    print(t, g)
