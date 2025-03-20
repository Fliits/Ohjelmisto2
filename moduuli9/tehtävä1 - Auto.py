class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nyknopeus = 0
        self.matka = 0

auto1 = Auto("ABC-123", 142)
print(f"Rekkari on {Auto.rekisteritunnus}, huippunopeus {Auto.huippunopeus} km/h")