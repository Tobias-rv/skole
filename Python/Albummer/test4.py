
def nyttAlbum():
    album = []
    sanger = []
    artister = []
    aNavn = str(input("Navn på ALbumet:"))
#Antall sanger og navn på sangene
    antS = int(input("Antall sanger:"))
    while len(sanger) < antS:
        sang = str(input("Skriv inn en sang:"))
        sanger.append(sang)
#Antall artister og navn på artistene
    antA = int(input("Antall artister:"))
    while len(artister) < antA:
        artist = str(input("Skriv navnet på en artist:"))
        artister.append(artist)
#Setter sanger og artister inn i samme liste
    alubm.append(aNavn)
    album.append(sanger)
    if 0 < antA:
        album.append(artister)

    print(album)
nyttAlbum()
