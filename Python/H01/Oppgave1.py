import math
def pi(dec = 2):
    if dec > 15:
        print("For mange decimaler")
        print(math.pi)
    else:
        print(round(math.pi, dec))
