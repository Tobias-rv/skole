class bibliotek:
    albumer = []
    def leggTil(self, album):
        self.albumer.append(album)
    def printBibliotek(self, navn = None):


class album:
    alNavn = ""
    artister = []
    sanger = []

    def __init__(self, navn):
        self.alNavn = alNavn
    def leggTilArtist(self, artist):
        self.artister.append(artist)
    def leggTilSanger(self, sang):
        self.sanger.append(sang)
