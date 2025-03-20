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
    def __init__(self, pohja, ylin, hissit):
        self.pohja = pohja
        self.ylin = ylin
        self.hissit = hissit
        self.elevators = []

        for i in range(1, self.hissit + 1):
            self.elevators.append(Hissi(self.pohja,self.ylin))

    def aja_hissiä(self, hissi, kerros):
        print('Hissin numero on ' + str(hissi))
        self.elevators[hissi].siirry_kerrokseen(kerros)

talo = Talo(0, 8, 5)
talo.aja_hissiä(4,7)
