# Najdaljši palindromski podniz
# Verzija, ki je na spletu
# https://www.programcreek.com/2013/12/leetcode-solution-of-longest-palindromic-substring-java/


def center(niz, zacetek, konec):
    '''Vrni začetni in končni indeks najdaljšega palindroma z danim centrom.'''
    while zacetek >= 0 and konec < len(niz): # Da ostanemo v besedi
        if niz[zacetek] == niz[konec]:
            zacetek -= 1
            konec += 1
        else:
            break
    return (zacetek + 1, konec)


def palindrom(niz):
    '''Vrni najdaljši palindromski podniz. Preizkusi vse možne centre.'''
    zacetekNajP = 0
    konecNajP = 0
    for zacCentra in range(len(niz)):
        for konCentra in (zacCentra, zacCentra + 1): # Center v enem ali dveh znakih
            (zacetek, konec) = center(niz, zacCentra, konCentra)
            if konec - zacetek > konecNajP - zacetekNajP:
                zacetekNajP = zacetek
                konecNajP = konec
    return niz[zacetekNajP:konecNajP]


########################### TESTI ############################

test1 = "banana"
test2 = "priimek"
test3 = "abba"
test4 = "pericarežeracirep"
test5 = "lisica"
1
# Vir za slovenske palindrome:
# http://bos.zrc-sazu.si/palindromi/index.html
test6 = "".join(["On red omili moderno.", "Oviran bo bobnar Ivo.", \
                 "O, mi le žogo želimo.", "Perica reže raci rep.", \
                 "Počešite teti še čop.", "Rad uredi bide rudar.", \
                 "Ceni plaho voh alpinec.", "Ceni plažo mož alpinec." \
                 "Ema Zvonku sukno vzame."]).replace(" ", "").lower()

for i in range(1, 7):
    print(eval("palindrom(test{0})".format(i)))

####################### END: TESTI ############################
