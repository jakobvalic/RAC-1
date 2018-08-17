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
kvadrat = 120 #stranica kvadrata v pikslih
visina = kvadrat * 8
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

def ustvariPolje(barva):
    '''Ustvari polje sodih dimenzij. Za lihe še ne deluje.'''
    for i in range(visina):
        # poskrbimo za ustrezno barvo pri menjavi vrstic
        if i % kvadrat ==  0:
            if barva == crna:
                barva = bela
            else:
                barva = crna

        for j in range(sirina):
            if j % kvadrat == 0:
                if barva == crna:
                    barva = bela
                else:
                    barva = crna
            if barva == bela:
                piksli[i][j] = 255
            platno.create_rectangle(j, i, j+1, i+1, fill=barva, outline = "" )
                # if sirina % 2 == 1: # Za matrike lihih dimenzij
                #     barva = crna if barva == bela else bela

ustvariPolje(crna)


def izMatrike(matrika):
    '''Nariše sliko iz matrike. 0 - črna, 255 - bela.'''
    for i in range(len(matrika)):
        for j in range(len(matrika[0])):
            barva = 'white' if matrika[i][j] == 255 else 'black'
            platno.create_rectangle(j, i, j+1, i+1, fill=barva, outline="")

# izMatrike(piksli)

# KODA ZA IZRIS VZORČENJA
def izrisiTocke(seznam):
    '''Izriše vzorčne točke.'''
    for (x, y) in seznam:
        x = 0 if (x - 2) < 0 else (x - 2)
        y = 0 if (y - 2) < 0 else (y - 2)
        platno.create_rectangle(x, y, x+4, y+4, fill='red', outline='')
    return seznam


def izrisVzorcenja(seznam, kvadrat_px):
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
    vsi_random = []
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
                vsi_random.append((vrst, stol))
                st+=1
            sez_j.append(sum(sez_nakljucnih)//stTock) # Izračunamo povprečje
        koncni_sez.append(sez_j)
    return koncni_sez, vsi_random


# Grid
def gridVzorci(matrika, vzorec, stTock):
    '''Na sliki naredi seznam grid vzorčenja.'''
    vsi_vzorci = []
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
                    vsi_vzorci.append((vrst, stol))
                    # print((vrst, stol), matrika[vrst][stol])
                    stevec_tock += 1
                    j += razmak
                i += razmak
            sez_j.append(sum(sez_grid) // stevec_tock)
        koncni_sez.append(sez_j)
    return koncni_sez, vsi_vzorci

# Jitter
def jitterVzorci(matrika, vzorec, stTock):
    '''Na sliki naredi seznam jitter vzorčenja.'''
    vsi_vzorci = []
    koncni_sez = []
    razmak = round(vzorec // sqrt(stTock))
    for vzorec_i in range(len(matrika) // vzorec):
        sez_j = []
        for vzorec_j in range(len(matrika[0]) // vzorec):
            sez_jitter = []
            st_tock = 0
            while st_tock < stTock:
                vrstica = randint(vzorec_i * vzorec, (vzorec_i + 1) * vzorec - 1)
                stolpec = randint(vzorec_j * vzorec, (vzorec_j + 1) * vzorec - 1)
                sez_jitter.append(matrika[vrstica][stolpec])
                vsi_vzorci.append((vrstica, stolpec))
                st_tock += 1
            sez_j.append(sum(sez_jitter) // stTock)
        koncni_sez.append(sez_j)
    return koncni_sez, vsi_vzorci

# PRIMERI

# Jitter
faktor_vzorca_jitter = 2

vzorciJitter, vsi_jitter = jitterVzorci(piksli, kvadrat * faktor_vzorca_jitter, 25)
print('Vzorci jitter:', vzorciJitter)
izrisiTocke(vsi_jitter)
# izrisVzorcenja(vzorciJitter, kvadrat * faktor_vzorca_jitter)
izrisVzorcenja([[102, 112, 153, 122], [142, 132, 102, 122], [132, 122, 142, 132], [153, 153, 132, 142]], kvadrat * faktor_vzorca_jitter)

# # Grid
#
# faktor_vzorca_grid  = 2
# vzorciGrid, vsi_grid = gridVzorci(piksli, kvadrat * faktor_vzorca_grid, 100)
# izrisiTocke(vsi_grid)
# # print('Vzorci grid:', vzorciGrid)
# izrisVzorcenja(vzorciGrid, kvadrat * sirina // kvadrat)


# Random

# vzorciRandom, vsi_random = nakljucniVzorci(piksli, kvadrat * 2, 25)
# print('Vzorci random:', vzorciRandom)
# izrisiTocke(vsi_random)
# # izrisVzorcenja(vzorci, kvadrat)
#
# print(izrisVzorcenja(vzorciRandom, kvadrat * 2))


mainloop()
