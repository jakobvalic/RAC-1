class Sklad:

    def __init__(self):
        '''Ustvari prazen sklad.'''
        self.podatki = []

    def vstavi(self, x):
        '''Na vrh sklada vstavi podatek x.'''
        self.podatki.append(x)

    def prazen(self):
        '''Vrne True, če je sklad prazen, sicer vrne False.'''
        return len(self.podatki) == 0

    def odstrani(self):
        '''Iz sklada odstrani vrhnji podatek. Če ga ni, sproži izjemo.'''
        if self.prazen():
            raise IndexError('ODSTRANI: Sklad je prazen.')
        del self.podatki[-1]

    def vrh(self):
        '''Vrne vrhnji podatek v skladu. Če ga ni, sproži izjemo.'''
        if self.prazen():
            raise IndexError('VRH: Sklad je prazen.')
        return self.podatki[-1]

    def poberi(self):
        '''Iz sklada odstrani in vrne vrhnji podatek. Če ga ni, sproži izjemo.'''
        if self.prazen():
            raise IndexError('POBERI: Sklad je prazen.')
        stari_vrh = self.vrh()
        self.odstrani()
        return stari_vrh

    def __str__(self):
        '''Vrne predstavitev sklada z nizom "DNO : x1 : ... : xn : VRH".'''
        opisi = ['DNO'] + [str(elt) for elt in self.podatki] + ['VRH']
        return ' : '.join(opisi)