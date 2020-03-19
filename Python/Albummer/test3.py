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

class Sang:
    saNavn = ""
    def __init__(self, saNavn):
        self.saNavn = saNavn

alNavn = str(input("Navn på Album:"))
nyttAlbum = Album(alNavn)

a = int(input("Hvor mange sanger er det i albumet?"))
x = 0
while x < a:
    saNavn = str(input("Hva heter sangen?"))
    nyttAlbum.legTilSang(saNavn)
    x = x + 1
