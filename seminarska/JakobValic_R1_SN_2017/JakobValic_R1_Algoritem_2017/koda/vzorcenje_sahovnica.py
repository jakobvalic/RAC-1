from tkinter import  *
from random import *
from math import *

#==============================
def pretovriVrednost(vr):
    "Pretvori eno vrednost iz RGB."

    Crke = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "g"}
    vrednosti1 = [128, 64, 32, 16, 8, 4, 2, 1]
    vrednosti2 = [0,0,0,0,0,0,0,0]
    crka = [8, 4, 2, 1]
    rez1 = 0
    rez2 = 0

    for i in range(0, 8):
        if vr // vrednosti1[i] > 0:
            vrednosti2[i] = 1
            vr = vr - vrednosti1[i]
        else:
            vrednosti2[i] = 0
    for j in range(0, 4):
        rez1 += crka[j] * vrednosti2[j]
        rez2 += crka[j] * vrednosti2[j + 4]

    if rez1 >= 10:
        rez1 = Crke[rez1]
    if rez2 >= 10:
        rez2 = Crke[rez2]

    return str(rez1) + str(rez2)
#====================================

#IZBRANI PODATKI:
kvadrat = 60 #stranica kvadrata v pikslih
visina = kvadrat * 6
sirina = visina


#Rišemo osnovno sliko

master = Tk()
platno = Canvas(master, width= sirina, height = visina)
platno.pack()

# Barve predstavimo z RGB lestvico
# rgb=(255,255,255)
bela = "white"
crna = "black"

barva = crna
piksli = [[0 for _ in range(sirina)] for _ in range(visina)] # Matrika črne barve

for i in range(0,visina,1):
    #poskrbimo za sutrezno barvo pri menjavi vrstic
    if i%kvadrat ==  0:
        if barva == crna:
            barva = bela
        else:
            barva = crna

    for j in range(0,sirina,1):
        if j%kvadrat == 0:
            if barva == crna:
                barva = bela
            else:
                barva = crna
        platno.create_rectangle(j, i, j+1, i+1, fill=barva, outline = "" )
        if barva == bela:
            piksli[i][j] = 255

# Preverimo:
# platno.create_rectangle(0, 0, kvadrat, kvadrat, fill='pink', outline = "")
# for vr in piksli:
#     print(vr)


def izMatrike(matrika):
    '''Nariše sliko iz matrike. 0 - črna, 255 - bela.'''
    for i in range(len(matrika)):
        for j in range(len(matrika[0])):
            barva = 'white' if matrika[i][j] == 255 else 'black'
            platno.create_rectangle(j, i, j+1, i+1, fill=barva, outline="")

# izMatrike(piksli)

# KODA ZA IZRIS VZORČENJA

def nakljucnoVzorcenje(seznam, kvadrat_px):
    vrstice = len(seznam)
    stolpci = len(seznam[0])
    for i in range(0,vrstice):
        for j in range(0,stolpci):
            b = seznam[i][j]
            ba = pretovriVrednost(b)
            barva = "#" + str(ba)*3
            platno.create_rectangle(j*kvadrat_px,i*kvadrat_px,(j+1)*kvadrat_px,(i+1)*kvadrat_px,fill = barva, outline="")
    return

# KODE ZA RAZLIČNA VZORČENJA

# Random

def nakljucniVzorci(matrika, vzorec, stTock):
    '''Na sliki, ki je podana z matriko pikslov, naredi random vzorčenje, izračuna povprečje vzorcev in vrne novo matriko
    glede na dobljene vzorce.'''

    koncni_sez =[]

    for i in range(len(matrika)//vzorec):
        sez_j =[]
        for j in range(len(matrika[0])//vzorec):
            sez_nakljucnih = []
            st = 0
            while st < stTock:
                vrst = randint(i*vzorec,(i+1)*vzorec-1)
                stol = randint(j*vzorec,(j+1)*vzorec-1)
                sez_nakljucnih.append(matrika[vrst][stol])
                st+=1
            sez_j.append(sum(sez_nakljucnih)//stTock) # Izračunamo povprečje
        koncni_sez.append(sez_j)
    return koncni_sez


# Grid
def gridVzorci(matrika, vzorec, stTock):
    '''Na sliki naredi seznam grid vzorčenja.'''
    koncni_sez = []
    razmak = round(vzorec // sqrt(stTock))
    for vzorec_i in range(len(matrika) // vzorec):
        sez_j = []
        for vzorec_j in range(len(matrika[0]) // vzorec):
            sez_grid = []
            i = vzorec_i * vzorec
            stevec_tock = 0
            while i < (vzorec_i + 1) * vzorec:
                j = vzorec_j * vzorec
                while j < (vzorec_j + 1) * vzorec:
                    vrst = i + (razmak // 2)
                    stol = j + (razmak // 2)
                    sez_grid.append(matrika[vrst][stol])
                    # print((vrst, stol), matrika[vrst][stol])
                    stevec_tock += 1
                    j += razmak
                i += razmak
            # print(sez_grid)
            sez_j.append(sum(sez_grid) // stevec_tock)
        koncni_sez.append(sez_j)
    return koncni_sez

# PRIMERI

# Grid
faktor_vzorca = 3 # Če damo 2, dobimo vse sivo

vzorciGrid = gridVzorci(piksli, kvadrat * faktor_vzorca, 700)
print('Vzorci grid:', vzorciGrid)
nakljucnoVzorcenje(vzorciGrid, kvadrat * faktor_vzorca)


# Random
vzorci = nakljucniVzorci(piksli, kvadrat*2, 9)
print('Vzorci random:', vzorci)
# izrisVzorcenja(vzorci, kvadrat*2)





mainloop()
