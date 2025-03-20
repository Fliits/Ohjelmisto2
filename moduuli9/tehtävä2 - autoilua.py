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

auto = Auto("ABC-123",142)
auto.kiihdytä(30)
print(auto.nyknopeus)
auto.kiihdytä(70)
print(auto.nyknopeus)
auto.kiihdytä(50)
print(auto.nyknopeus)
auto.kiihdytä(-200)
print(auto.nyknopeus)