import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nyknopeus = 0
        self.matka = 0

    def kiihdytä(self,nopeus):
        uusinopeus = 0
        self.nyknopeus += nopeus
        if uusinopeus < 0:
            self.nyknopeus = 0
        if self.nyknopeus > self.huippunopeus:
            self.nyknopeus = self.huippunopeus
        return
    def kulje(self,aika):
        self.matka += self.nyknopeus * aika
        return

autot = []
matka = 0

for i in range(0,10):
    autot.append(f'auto{i+1}')
    nopeus = random.randint(100, 200)
    autot[i] = Auto(f"ABC-{i+1}", nopeus)
    matka = autot[i].matka

while matka < 10000:
    for a in autot:
        kiihtyvyys = random.randint(-10,15)
        #print(kiihtyvyys) tarkistus että muuttuja voi myös olla negatiivinen
        a.kiihdytä(kiihtyvyys)
        a.kulje(1)
        if a.matka > matka:
            matka = a.matka

for a in autot:
    print(f'{a.rekisteritunnus}: {a.huippunopeus}km/h {a.nyknopeus}km/h {a.matka}km')