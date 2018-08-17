class Graf:

    def __init__(self):
        self.vozli = {}
        self.pregled_v = {}
        self.povezave = set()
        self.not_dfs = set()
        self.v_verigi = set()

    def dodaj_povezavo(self, x, y):
        self.vozli[x] = self.vozli.get(x, set()).union({y})
        self.vozli[y] = self.vozli.get(y, set()).union({x})
        self.pregled_v[x] = (None, False)
        self.pregled_v[y] = (None, False)
        povezava = (min(x, y), max(x, y))
        self.povezave = self.povezave.union({povezava})
        self.not_dfs = self.not_dfs.union({povezava})

    def dodaj_vozel(self, x):
        if x in self.vozli.keys():
            pass
        else:
            self.vozli[x] = []
            self.pregled_v[x] = (False, False)

    def __str__(self):
        if len(self.vozli) == 0:
            return "Prazen graf."
        else:
            niz = "Vozli: \n"
            for i in self.vozli.keys():
                niz += str(i) + "_"
            niz += "\n"
            niz += "Povezave: \n"
            for k in self.povezave:
                niz += str(k) + "\n"
        return niz

# preveri, če je še kako nepregledano vozlišče.
# če obstaja vrnemo to vozlišče
# sicer ne vrnemo ničesar (None)
def najdi_zacetek(graf):
    for i in graf.pregled_v.keys():
        i1, _ = graf.pregled_v[i]
        if not i1:
            graf.pregled_v[i] = (1, False)
            return i

# for zanka išče nepregledane sosede
# če najde se izvede if
# nepregledanemu sosedu se priredi število
# povezavo med začetkom in sosedom odstranimo iz nepregledanih povezav
# za konec se vrne dfs_pregled soseda
# če ne najde poskušaš iti nazaj (v soseda z nižjo številko)
# če ga najdeš vrneš dfs_pregled tega soseda
# če takega soseda ni je pregled opravljen in vrneš samo graf.
def dfs_pregled(graf, zacetek, n=1):
    for i in graf.vozli[zacetek]:
        i1, _ = graf.pregled_v[i]
        if not i1:
            graf.pregled_v[i] = (n+1, False)
            graf.not_dfs.remove((min(zacetek, i), max(zacetek, i)))
            return dfs_pregled(graf, i, n+1)
        else:
            pass
    n0, _ = graf.pregled_v[zacetek]
    if n0 != 1:
        nn = 0
        for i in graf.vozli[zacetek]:
            i0, _ = graf.pregled_v[i]
            if (min(zacetek, i),max(zacetek, i)) not in graf.not_dfs and i0 < n0:
                nn = max(i0,nn)
                ix = i
        return dfs_pregled(graf, ix, n)
    return graf

# se izvaja, dokler niso vsa vozlišča pregledana
# z drugimi besedami:
# se izvaja, dokler je funkcija najdi_zacetek sposobna najti nov zacetek
def prvi_pregled(graf):
    zac = najdi_zacetek(graf)
    while zac:
        graf = dfs_pregled(graf, zac)
        zac = najdi_zacetek(graf)
    return graf


# funkcija ustvarja verige
# vse povezave, ki so del katerekoli verige, najdemo v graf.v_verigi
# zanka while se izvaja, dokler ne dosežemo že obiskanega vozla
# zanka for se izvaja zato, da najdemo sosednji vozel, ki je oštevilčen
# z najvišjim številom izmed tistih, ki so manjša od števila, s katerim
# je označen vozel, v katerem se nahajamo.

def veriga(graf, povezava):
    x,y = povezava
    graf.v_verigi.add((x,y))
    x1, x2 = graf.pregled_v[x]
    graf.pregled_v[x] = (x1, True)
    y1, y2 = graf.pregled_v[y]
    while not y2:
        graf.pregled_v[y] = (y1, True)
        naslednji = x
        for k in graf.vozli[y]:
            k1, _ = graf.pregled_v[k]
            i1, _ = graf.pregled_v[naslednji]
            if k1 < y1:
                if k1 > i1:
                    naslednji = k
        graf.v_verigi.add((min(y,naslednji),max(y,naslednji)))
        y = naslednji
        y1, y2 = graf.pregled_v[y]
    return graf

# za drugi pregled mora biti levo krajišče povezave oštevilčeno
# z manjšim naravnim številom kot desno krajišče povezave
# to uredi prva for zanka
# potem množico tuplov spremenimo v seznam tuplov, da uporabimo sort.
# kar nam olajša delo
# ko delamo verige moramo namreč najrej porabiti tisti par, ki vsebuje
# najnižje oštevilčeno vozlišče.
def drugi_pregled(graf):
    for x,y in graf.not_dfs:
        x1,_ = graf.pregled_v[x]
        y1,_ = graf.pregled_v[y]
        if y1 < x1:
            graf.not_dfs.remove((x,y))
            graf.not_dfs.add((y,x))
    graf.not_dfs = list(graf.not_dfs)
    graf.not_dfs.sort()
    for x,y in graf.not_dfs:
        veriga(graf, (x,y))
    return graf

def mostovi(graf):
    prvi_pregled(graf)
    drugi_pregled(graf)
    graf.v_verigi
    for x,y in graf.v_verigi:
        if x != min(x,y):
            graf.v_verigi.remove((x,y))
            graf.v_verigi.add((y,x))
    return graf.povezave.difference(graf.v_verigi)


# slabost: funkcije spreminjajo direktno graf g in ne njegove kopije
# nekaj for zank, ki se zdijo popolnoma nepotrebne
###Primer
g = Graf()
g.dodaj_povezavo("e","i")
g.dodaj_povezavo("e","j")
g.dodaj_povezavo("i","j")
g.dodaj_povezavo("i","n")
g.dodaj_povezavo("m","n")
g.dodaj_povezavo("j","n")
g.dodaj_povezavo("j","k")
g.dodaj_povezavo("l","k")
g.dodaj_povezavo("o","k")
g.dodaj_povezavo("o","l")
g.dodaj_povezavo("o","p")
g.dodaj_povezavo("p","l")
g.dodaj_povezavo("a","b")
g.dodaj_povezavo("c","d")
g.dodaj_povezavo("c","g")
g.dodaj_povezavo("h","g")
g.dodaj_vozel("f")
print(mostovi(g))
