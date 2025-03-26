class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"{self.nimi} -julkaisun päätoimittaja on {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.nimi} -kirjan kirjoitti {self.kirjailija}, ja siinä on {self.sivumäärä} sivua")

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti Nro. 6", "Rosa Liksom", 200)
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()