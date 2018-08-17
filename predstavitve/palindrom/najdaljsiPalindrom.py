# Najdaljši palindromski podniz
# https://www.programcreek.com


def center(niz, zacetek, konec):
    '''Poišče najdaljši palindrom z danim centrom.'''
    while zacetek >= 0 and konec < len(niz): # Da ostanemo v besedi
        if niz[zacetek] == niz[konec]:
            zacetek -= 1
            konec += 1
        else:
            break
    return niz[zacetek+1:konec]


def palindrom(niz):
    '''Poišče najdaljši palindrom v nizu.'''
    najP = ""
    for i in range(len(niz)):
        center1 = center(niz, i, i) # Center v enem znaku
        if len(center1) > len(najP):
            najP = center1
        center2 = center(niz, i, i+1) # Center v dveh sosednjih znakih
        if len(center2) > len(najP):
            najP = center2
    return najP












# ============================================
# testi

test1 = "lisica"
test2 = "banana"
test3 = "abba"
test4 = "pericarežeracirep"

test5 = "".join(["On red omili moderno.", "Oviran bo bobnar Ivo.", \
                 "O, mi le žogo želimo.", "Perica reže raci rep.", \
                 "Počešite teti še čop.", "Rad uredi bide rudar.", \
                 "Ceni plaho voh alpinec.", "Ceni plažo mož alpinec." \
                 "Ema Zvonku sukno vzame."]).replace(" ", "").lower()

for i in range(1, 6):
    print(eval("palindrom(test{0})".format(i)))


# ============================================
# test hmp


with open("HisaMarijePomocnice.txt", "r") as f:
    hmpCela = f.readlines()

hmp = ""
for vr in hmpCela:
    hmp += vr.strip()

hmp = ''.join(hmp.split(" ")).lower()

# print(palindrom(hmp))






