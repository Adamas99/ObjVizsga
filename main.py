from datetime import datetime, timedelta
from szoba import EgyagyasSzoba, KetagyasSzoba
from szalloda import Szalloda
from foglalas import Foglalas

def main():
    szalloda = Szalloda("Hotel Budapest")
    print(f"Üdvözöli a {szalloda.nev}!")

    szalloda.szoba_hozzaad(EgyagyasSzoba(1))
    szalloda.szoba_hozzaad(KetagyasSzoba(2))
    szalloda.szoba_hozzaad(EgyagyasSzoba(3))

    jovo_nap = datetime.today().date() + timedelta(days=1)
    for i in range(5):
        szalloda.foglalas(szalloda.szobak[i % 3], jovo_nap + timedelta(days=i))

    while True:
        print("\n--- Hotel Szobafoglaló Rendszer ---")

        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Listázás")
        print("4. Kilépés")
        valasztas = input("Válasszon a fentiekből: ")

        if valasztas == "1":
            # Foglalás létrehozása
            szobaszam = int(input("Adja meg a szobaszamot (1-3 ig választhat): "))
            if szobaszam not in [1, 2, 3]:
                print("Nem létezik ez a szoba.")
                continue
            nap = input("Adja meg a napot (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                nap = datetime.strptime(nap, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum. Kérjük, használja az ÉÉÉÉ-HH-NN formátumot.")
                continue
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    eredmeny = szalloda.foglalas(szoba, nap)
                    print(eredmeny)
        elif valasztas == "2":
            # Foglalás lemondása
            szobaszam = int(input("Adja meg a szobaszámot: "))
            nap = input("Adja meg a napot (YYYY-MM-DD formátumban): ")
            try:
                nap = datetime.strptime(nap, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum. Kérjük, használja az ÉÉÉÉ-HH-NN formátumot.")
                continue
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.nap == nap:
                    eredmeny = szalloda.lemondas(foglalas)
                    print(eredmeny)
        elif valasztas == "3":
            szalloda.listazas()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    main()