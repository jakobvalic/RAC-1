import random

def izpis(matrika):
    '''Izpiše matriko po vrsticah.'''
    for vr in matrika:
        print(vr)

def priprava(dim):
    '''Pripravi osnovno otočje v obliki matrike.'''
    otočje = [[int(round(random.random())) for _ in range(dim)] for _ in range(dim)]
    return otočje

# Pomožna funkcija

def dfs(graf, i, j):
    '''Enice otoka, v katerem se nahaja enica na mestu (i, j) spremeni v ničle.'''
    graf[i][j] = 0
    # Pregledamo v vse štiri smeri npr. (-1, 0) je levo
    smeri = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    for (vodoravno, navpicno) in smeri:
        n = i + vodoravno
        m = j + navpicno
        if 0 <= n < len(graf) and 0 <= m < len(graf[0]) and graf[n][m] == 1:
            dfs(graf, n, m)

# Glavna funkcija

def koliko_otokov(graf, izpis_grafa):
    '''Vrne število otokov, to je povezanih enic v grafu.'''
    stevilo_otokov = 0
    print("Osnovni zemljevid:")
    izpis(graf)
    for i in range(len(graf)):
        for j in range(len(graf[0])):
            if graf[i][j] == 1: # Našli smo del otoka
                stevilo_otokov += 1
                if izpis_grafa:
                    input('\n {}. Zbrisali bomo otok \n'.format(stevilo_otokov))
                dfs(graf, i, j) # Poženemo dfs, da zbrišemo cel otok
                if izpis_grafa:
                    izpis(graf)
    return stevilo_otokov

# Testi

otocje = [[0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 0]]

print('Število otokov na zemljevidu je: {}.'.format(koliko_otokov(otocje, True)), '\n')


while True:
    try:
        dim = int(input('Vnesi dimenzijo otoka: '))
        izpis_grafa = False if dim > 8 else True
        otočje = priprava(dim)
        print('Število otokov na zemljevidu je: {}.'.format(koliko_otokov(otočje, izpis_grafa)), '\n')
    except ValueError as e:
        print('Vnesite veljavno dimenzijo otoka!')
        





            
