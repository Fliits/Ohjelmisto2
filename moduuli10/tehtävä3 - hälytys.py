class Hissi:
    def __init__(self, pohja, ylin):
        self.pohja = pohja
        self.ylin = ylin
        self.kerros = 0

    def siirry_kerrokseen(self, uusi):
        while self.kerros > uusi:
            self.kerros_alas()
        while self.kerros < uusi:
            self.kerros_ylös()

    def kerros_ylös(self):
        self.kerros += 1
        print(f'Hissi on kerroksessa: {self.kerros}')

    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi on kerroksessa: {self.kerros}')

class Talo:
    def __init__(self, pohja, ylin, hissimäärä):
        self.pohja = pohja
        self.ylin = ylin
        self.hissimäärä = hissimäärä
        self.hissit = []

        for i in range(1, self.hissimäärä + 1):
            self.hissit.append(Hissi(self.pohja,self.ylin))

    def aja_hissiä(self, hissi, kerros):
        print('Hissin numero on ' + str(hissi))
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(0)
            print('Hissi on pohjakerroksessa')

talo = Talo(0, 8, 5)
talo.aja_hissiä(4,7)
talo.aja_hissiä(1,4)
talo.aja_hissiä(3,3)
talo.aja_hissiä(2,5)
talo.aja_hissiä(0,6)
talo.palohälytys()