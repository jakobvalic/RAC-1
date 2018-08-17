# Kattis, vsi palindromi

import sys

def center(niz, zacetek, konec):
    '''Poišče najdaljši palindrom s centrom v i.'''
    vsiP = set()
    if len(niz) <= 1:
        return vsiP
    while zacetek >= 0 and konec < len(niz):
        if niz[zacetek] == niz[konec]:
            # print(niz[zacetek], niz[konec])
            vsiP.add(niz[zacetek:konec+1])
            # print(vsiP)
            zacetek -= 1
            konec += 1
        else:
            break
    return vsiP


def palindrom(niz):
    '''S pomočjo pomožne funkcije center poišče vse palindrome v nizu.'''
    vsiP = set()
    for i in range(len(niz)):
        vsiP = vsiP.union(center(niz, i, i))
        vsiP = vsiP.union(center(niz, i, i+1))
    for p in sorted(list(vsiP)):
        if len(p) > 1:
            print(p)
    

for line in sys.stdin:
    palindrom(line.strip())
