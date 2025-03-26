import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nyknopeus = 0
        self.matka = 0

    def kiihdytä(self,muutos):
        self.nyknopeus += muutos
        if self.nyknopeus < 0:
            self.nyknopeus = 0
        if self.nyknopeus > self.huippunopeus:
            self.nyknopeus = self.huippunopeus
        return

    def kulje(self,aika):
        self.matka += self.nyknopeus * aika
        return

    def nopeus(self, nopeus):
        self.nyknopeus = nopeus
        return

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,  bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        print("Tunti kuluu...")
        for a in self.osallistujat:
            #kiihtyvyys = random.randint(-10, 15)
            # print(kiihtyvyys) tarkistus että muuttuja voi myös olla negatiivinen
            #a.kiihdytä(kiihtyvyys)
            a.kulje(aika)


    def tulosta_tilanne(self):
        self.osallistujat.sort(key=lambda a: a.nyknopeus, reverse=True)
        for a in self.osallistujat:
            print(f'{a.rekisteritunnus}: {a.huippunopeus}km/h {a.nyknopeus}km/h {a.matka}km')

    def kilpailu_ohi(self):
        for a in self.osallistujat:
            if a.matka >= self.pituus:
                print(f"Voittaja on {a.rekisteritunnus}")
                return True
        return False


autot = []
aika = 0
matka = 0

#for i in range(0,10):
#    autot.append(f'auto{i+1}')
#    hnopeus = random.randint(100, 200)
#    autot[i] = Auto(f"ABC-{i+1}", hnopeus)

sähkönen = Sähköauto("ABC-15", 180, 52.5)
sähkönen.nopeus(100)
bensanen = Polttomoottoriauto("ACD-123", 165, 32.3)
bensanen.nopeus(90)
autot.append(sähkönen)
autot.append(bensanen)

kisa = Kilpailu("Suuri romuralli", 8000, autot)

while aika < 3:
    kisa.tunti_kuluu()
    aika += 1

#while not kisa.kilpailu_ohi():
#
#    kisa.tunti_kuluu()
#
#    aika += 1
#    #if aika % 10 == 0:
#    kisa.tulosta_tilanne()
#
kisa.tulosta_tilanne()

