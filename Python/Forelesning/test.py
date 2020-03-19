s = input("Skriv in Sekunder:\n")
m = input("Skriv in Minutter:\n")
t = input("Skriv in Timer:\n")
s = int(s)
m = int(m)
t = int(t)
while s > 60:
    s = s - 60
    m = m + 1
while m > 60:
    m = m - 60
    t = t + 1
print("Tiden er:\n",t,"t", m,"m", s,"s")
