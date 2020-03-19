#Temaoppgave1 for Tobias Rosmer Vuttudal

#Oppgaver 1-3

#oppgave 1a
print ("Tobias\nRosmer\nVuttudal")

print()
#Oppgave 1b
print ('Tobias','Rosmer','Vuttudal', sep='\n')

print()
#Oppgave 2
print ('*****   ***   ****   *    *     *****\n  *    *   *  *   *  *   * *    *\n  *    *   *  ****   *  *****   *****\n  *    *   *  *   *  *  *   *       *\n  *     ***   ****   *  *   *   *****')

print()
#Oppgave 3a
nok = input('Beløp i NOK:')
nok = float(nok)
e = nok/9.76
d = nok/8.61
e = round(e, 2)
d = round(d, 2)


print(nok, ' kroner tilsvarer',e,' Euro',d,' Dollar')

#oppgave 3b
nok = input('Beløp i NOK:')
nok = float(nok)
e = nok/9.76
d = nok/8.61
e = round(e, 2)
d = round(d, 2)


print(nok, ' kroner tilsvarer',e, u'\N{euro sign}', d,u'\N{dollar sign}')
