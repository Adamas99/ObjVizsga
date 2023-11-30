
from datetime import datetime
from foglalas import Foglalas

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szoba, nap):
        if nap < datetime.today().date():
            return "Rossz dátum. A foglalás dátuma nem lehet korabbi, mint a mai nap."
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.nap == nap:
                return "A szoba már foglalt ebben az időpontban, válasszon másik időpontot."
        foglalas = Foglalas(szoba, nap)
        self.foglalasok.append(foglalas)
        return "A foglalás sikeres. Köszönjük!"

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return "A foglalás lemondása sikeres."
        else:
            return "A foglalás nem található."

    def listazas(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Nap: {foglalas.nap}")