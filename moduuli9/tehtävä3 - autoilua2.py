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

auto = Auto("ABC-123",142)
auto.kiihdytä(30)
syöte = float(input(f"Auton nykynopeus on: {auto.nyknopeus}, kuinka kauan auto liikkuu?\n"))
auto.kulje(syöte)
print(auto.matka)
