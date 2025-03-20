class Hissi:
    def __init__(self, pohja, ylin):
        self.pohja = pohja
        self.ylin = ylin
        self.kerros = 0

    def siirry_kerrokseen(self, uusi):
        if uusi < self.pohja or uusi > self.ylin:
            print("Kerrosta ei ole")
            return
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

hissi = Hissi(0, 8)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(0)