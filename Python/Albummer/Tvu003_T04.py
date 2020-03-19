class Bibliotek:
    albumer = []
    def leggTil(self, album):
        self.albumer.append(album)
    def printBibliotek(self, navn = None):
        for a in self.albumer:
            if navn == None or navn == a.navn():
                a.printAlbum()



class Album:
    alNavn = ""
    sanger = []
    artister = []
    serieNr = []
    def __init__(self, alNavn):
        self.alNavn = alNavn
    def legTilSang(self, sang):
        self.sanger.append(sang)
    def leggTilArtist(self, artist):
        self.artister.append(artist)
    def leggTilSerieNr(self, nr):
        self.serieNr.append(nr)
    def navn(self):
        return self.alNavn
    def printAlbum(self):
        print("Album: " + self.alNavn)
        for s in self.sanger:
            print(s.navn())
        print("\n")

class Artist:
    arNavn = ""
    medlemmer = []
    def __init__(self, arNavn):
        self.arNavn = arNavn
    def leggTilMedlemmer(self, medlem):
        self.medlemmer.append(medlem)

class Sang:
    saNavn = ""
    komponister = []
    def __init__(self, saNavn):
        self.saNavn = saNavn
    def leggTilKomponist(self, komponist):
        self.komponister.append(komponist)
    def navn(self):
        return self.saNavn

serieNr = 1
bib = Bibliotek()
while True:
    v = int(input("Velg hva du vil gjøre\n1. Søke opp album\n2. Legge til nytt album\n"))
    if v == 1:
        v = str(input("Hvem ønsker du å finne?"))
        bib.printBibliotek(v)
    else:


        alNavn = str(input("Navn på Album:"))
        nyttAlbum = Album(alNavn)

        nyttSerieNr = Album(serieNr)
        nyttSerieNr.leggTilSerieNr(nyttSerieNr)
        serieNr = serieNr + 1

        arNavn = str(input("Hva er Artistnavnet/Gruppenavnet?"))
        nyArtist = Artist(arNavn)

        a = int(input("Hvor mange medlemmer er det?"))
        x = 0
        while x < a:
            nyMedlem = str(input("Navn på medlem:"))
            nyArtist.leggTilMedlemmer(nyMedlem)
            x = x + 1
        nyttAlbum.leggTilArtist(nyArtist)

        a = int(input("Hvor mange sanger er det i albumet?"))
        x = 0
        while x < a:
            saNavn = str(input("Hva heter sangen?"))
            nySang = Sang(saNavn)
            b = input("Ønsker du å legge til komponist?[y/n]")
            if b == "y":
                c = int(input("Hvor mange?"))
                z = 0
                while z < c:
                        koNavn = str(input("Navn på komponist:"))
                        nySang.leggTilKomponist(koNavn)
                        z = z + 1
            nyttAlbum.legTilSang(nySang)
            x = x + 1

        nyttAlbum.leggTilSerieNr(nyttSerieNr)

        bib.leggTil(nyttAlbum)
