class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        niz = ""
        for i in self.children:
            niz += str(i) + ", "
        if len(niz)>0:
            niz = niz[:len(niz)-2]
            return "Node "+str(self.data) + "[" + niz + "]"
        else:
            return "Node "+str(self.data)

# vrstni red dodajanja otrok je zelo pomemben!
# oce je koren drevesa!

# pomozna
def obratni_pregled_generator(oce):
    for i in oce.children:
        yield from obratni_pregled_generator(i)
    yield oce

# drevesu priredi obraten pregled
def obratni_pregled(oce):
    s=[]
    for i in obratni_pregled_generator(oce):
        s.append(i)
    return s

# prešteje število otrok izbranega vozlišča
def stevilo_otrok(vozlisce):
    n = 1
    for i in vozlisce.children:
        n += stevilo_otrok(i)
    return n


##### podatek oče je pomemben zaradi obratnega pregleda
##### le enkrat lahko uporabimo le eno od povezav, ki niso del drevesa
def nizko_stevilo(oce, vozlisce, seznam_povezav):
    pregled = obratni_pregled(oce)
    stevilo = pregled.index(vozlisce) + 1
    k=0
    while k < len(seznam_povezav):
        x,y = seznam_povezav[k]
        if x == vozlisce:
            stevilo_0 = nizko_stevilo(oce, y, [])
            if stevilo_0 < stevilo:
                return min(nizko_stevilo(oce, vozlisce, seznam_povezav[:k] + seznam_povezav[k+1:]), stevilo_0)
        elif y == vozlisce:
            stevilo_0 = nizko_stevilo(oce, x, [])
            if stevilo_0 < stevilo:
                return min(nizko_stevilo(oce, vozlisce, seznam_povezav[:k] + seznam_povezav[k+1:]), stevilo_0)
        k += 1
    for i in vozlisce.children:
        stevilo = min(stevilo,nizko_stevilo(oce, i, seznam_povezav))
    return stevilo

##### podatek oče je pomemben zaradi obratnega pregleda
##### le enkrat lahko uporabimo le eno od povezav, ki niso del drevesa
def visoko_stevilo(oce, vozlisce, seznam_povezav):
    pregled = obratni_pregled(oce)
    stevilo = pregled.index(vozlisce) + 1
    k=0
    while k < len(seznam_povezav):
        x,y = seznam_povezav[k]
        if x == vozlisce:
            stevilo_0 = visoko_stevilo(oce, y, [])
            if stevilo_0 > stevilo:
                stevilo = max(visoko_stevilo(oce, vozlisce, seznam_povezav[:k] + seznam_povezav[k+1:]), stevilo_0)
        elif y == vozlisce:
            stevilo_0 = visoko_stevilo(oce, x, [])
            if stevilo_0 > stevilo:
                stevilo = max(visoko_stevilo(oce, vozlisce, seznam_povezav[:k] + seznam_povezav[k+1:]), stevilo_0)
        k += 1
    for i in vozlisce.children:
        stevilo = max(stevilo,visoko_stevilo(oce, i, seznam_povezav))
    return stevilo
        

# ta funkcija samo združi podatke in jih da v seznam,
# da je vse bolj pregledno
def peterice(oce, seznam_povezav):
    pregled = obratni_pregled(oce)
    st_otrok = []
    niz_st = []
    vis_st = []
    sez_peteric = []
    k = 1
    for i in pregled:
        st_otrok.append(stevilo_otrok(i))
        niz_st.append(nizko_stevilo(oce, i, seznam_povezav))
        vis_st.append(visoko_stevilo(oce, i, seznam_povezav))
        sez_peteric.append((i.data, k, st_otrok[-1], niz_st[-1], vis_st[-1]))
        k += 1
    return sez_peteric

# račun, ki nam določi, katere povezave so mostovi
def mostovi(sez_peteric):
    resitve = []
    k = 0
    while k < len(sez_peteric)-1:
        (a,b,c,d,e) = sez_peteric[k]
        if e <= b and d > b-c:
            resitve.append(a)
        k += 1
    return resitve
            

##################################################
### https://www.youtube.com/watch?v=K2rkXGltHXQ
##
##a=Node("a")
##b=Node("b")
##c=Node("c")
##d=Node("d")
##e=Node("e")
##f=Node("f")
##g=Node("g")
##a.add_child(b)
##a.add_child(c)
##c.add_child(d)
##d.add_child(e)
##e.add_child(f)
##e.add_child(g)
##
##pet = peterice(a,[(b,d),(f,g)])
##print(pet)
##print(mostovi(pet))

##################################################
##      1
##     / \
##    3   4
##   / \   \
##  9   7   8
## /   /   /
##5---6   2

print("\n")

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
h=Node(8)
i=Node(9)
a.add_child(c)
a.add_child(d)
c.add_child(i)
c.add_child(g)
i.add_child(e)
g.add_child(f)
d.add_child(h)
h.add_child(b)

pet = peterice(a,[(e,f)])
print(pet)
print(mostovi(pet))

##################################################
##      1
##     / \
##    3   4
##   / \   \
##  9   7   8
## /   /   /
##5   6   2    povezava (5,8)

print("\n")

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
h=Node(8)
i=Node(9)
a.add_child(c)
a.add_child(d)
c.add_child(i)
c.add_child(g)
i.add_child(e)
g.add_child(f)
d.add_child(h)
h.add_child(b)

pet = peterice(a,[(e,h)])
print(pet)
print(mostovi(pet))

#################################################

##a=Node(1)
##b=Node(2)
##c=Node(3)
##d=Node(4)
##e=Node(5)
##f=Node(6)
##g=Node(7)
##h=Node(8)
##i=Node(9)
##a.add_child(c)
##a.add_child(d)
##c.add_child(i)
##c.add_child(f)
##i.add_child(e)
##f.add_child(g)
##h.add_child(b)
##d.add_child(h)

###################################################

print("\n")

a=Node(0)
b=Node(1)
c=Node(2)
d=Node(3)
e=Node(4)
f=Node(5)
g=Node(6)
b.add_child(a)
b.add_child(c)
b.add_child(d)
b.add_child(e)
b.add_child(g)
d.add_child(f)

pet = peterice(b,[(a,c),(e,f)])
print(pet)
print(mostovi(pet))

# https://stackoverflow.com/questions/2482602/a-general-tree-implementation
