# moje izrazoslovje je še vedno slabo
# primer: slovar={1:[2,3,4],2:[1,3],3:[1,2,6],4:[1,5],5:[4],6:[3],7:[],8:[9],9:[8]}
# rešitev: most(slovar)

def odstrani_kljuc(graf, kljuc):
    graf_0 = {}
    for k in graf:
        if k == kljuc:
            pass
        else:
            graf_0[k] = graf[k]
    return graf_0

# funkcija povezani bo preverila, koliko povezanih komponent imamo
# k naj bodo vsa vozlišča, ki so med seboj povezana
# n bodi število povezanih komponent
def povezani(graf, k = set(), n = 0):
    if graf == {}:
        return n
    else:
        if k == set():
# iščemo začetko točko neke nove povezane komponente.
            for i in graf.keys():
                zacetek = i
                break
            return povezani(graf, k.union({zacetek}), n+1)
        else:
# iščemo še nepregledano vozlišče iz množice k
            zacetek = 0.5
            for i in k:
                if i in graf.keys():
                    zacetek = i
                    break
            if zacetek is not 0.5:
# našli smo nepregledano vozlišče "zacetek"
# vse vrednosti ključa "zacetek" damo v k in izbrišemo ključ "zacetek"
                novi_cleni = graf[zacetek]
                novi_graf = odstrani_kljuc(graf, zacetek)
                return povezani(novi_graf, k.union(set(novi_cleni)), n)
            else:
# to se izvede, ko najdemo vse elemente povezane komponente
                return povezani(graf, set(), n)

def odstrani_povezavo(graf,kljuc,vrednost):
    graf_0 = {}
    for k in graf:
        if k != kljuc and k != vrednost:
            graf_0[k] = graf[k]
        elif k == kljuc:
            i = graf[k].index(vrednost)
            graf_0[k] = graf[k][:i] + graf[k][i+1:]
        elif k == vrednost:
            i = graf[k].index(kljuc)
            graf_0[k] = graf[k][:i] + graf[k][i+1:]       
    return graf_0

# funkcija most bo vrnila seznam vseh povezav, ki so most
def most(graf):
    resitev = []
    for kljuc in graf:
        for vrednost in graf[kljuc]:
# zaradi tega koraka je definirana funkcija odstrani_povezavo
            graf_0 = odstrani_povezavo(graf,kljuc,vrednost)
            if povezani(graf_0) != povezani(graf) and (vrednost,kljuc) not in resitev:
                resitev.append((kljuc,vrednost))
    return resitev


#primer cikla: slovar={1:[2,3],2:[1,4],3:[1,5],4:[2,5],5:[3,4]}

# primeri iz https://www.geeksforgeeks.org/bridge-in-a-graph/
# graf1={0:[1,2,3],1:[0,2],2:[0,1],3:[0,4],4:[3]}
# graf2={0:[1,2],1:[0,2,3,4,6],2:[0,1],3:[1,5],4:[1,5],5:[3,4],6:[1]}
# graf3={0:[1],1:[0,2],2:[1,3],3:[2]}

# primer iz http://lokar.fmf.uni-lj.si/www/R1-predstavitve-201617/predstavitev_Kosmač.pdf
# slovar = {1:[2,6],2:[1,6],3:[4,5],4:[3,5],5:[3,4,6],6:[1,2,5,7],7:[6,12,13],8:[9,10],9:[8,11],10:[8,11],11:[9,10,12],12:[11,7,13],13:[7,12]}

# graf_x={1:[2],2:[1],3:[4,5],4:[3],5:[3,6],6:[5],7:[8,9],8:[7,9,14],9:[7,8,10,14],10:[9,11,12],11:[10,12,13],12:[10,11,13],13:[12,11],14:[8,9,15],15:[14],16:[]}
