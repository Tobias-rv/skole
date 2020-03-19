class Album:
    sanger = []
    artister = []
    serieNr = []
    alNavn = ""
    def __init__(self, alNavn):
        self.alNavn = alNavn
    def legTilSang(self, sang):
        self.sanger.append(sang)
    def leggTilArtist(self, artist):
        self.artister.append(artist)

class Artist:
    arNavn = ""
    medlemmer = []
    def __init__(self, arNavn):
        self.arNavn = arNavn
    def leggTilMedlemmer(self, medlem):
        self.medlemmer.append(medlem)

    arNavn = str(input("Hva er Artistnavnet/Gruppenavnet?"))
    nyArtist = Artist(arNavn)

    a = int(input("Hvor mange medlemmer er det?"))
    x = 0
    while x < a:
        meNavn = str(input("Navn på medlem:"))
        nyArtist.leggTilMedlemmer(nyMedlem)
        x = x + 1
