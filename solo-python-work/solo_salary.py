import csv


class Pracownik:

    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def __str__(self):
        pracownik_info = f"""
        Imie: {self.imie}
        Nazwisko: {self.nazwisko}
        Wynagrodzenie_brutto: {self.wynagrodzenie_brutto}
        """
        return pracownik_info.strip()

    def oblicz_wynagrodzenie_netto(self):
        skladki = self.oblicz_skladki()
        wynagrodzenie_netto = self.wynagrodzenie_brutto - skladki
        return wynagrodzenie_netto

    def oblicz_skladki(self):
        skladki_zus_emerytalne = self.wynagrodzenie_brutto * 0.0976
        skladki_zus_rentowe = self.wynagrodzenie_brutto * 0.015
        skladki_zus_chorobowe = self.wynagrodzenie_brutto * 0.0245
        skladki_ubezpieczenie_zdrowotne = self.wynagrodzenie_brutto * 0.09
        skladki_fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        skladki_fgsp = self.wynagrodzenie_brutto * 0.001
        skladki_fep = self.wynagrodzenie_brutto * 0.015
        skladki = (
            skladki_zus_emerytalne +
            skladki_zus_rentowe +
            skladki_zus_chorobowe +
            skladki_ubezpieczenie_zdrowotne +
            skladki_fundusz_pracy +
            skladki_fgsp +
            skladki_fep
        )
        return skladki

    def oblicz_koszty(self):
        skladki_zus_emerytalne = self.wynagrodzenie_brutto * 0.0976
        skladki_zus_rentowe = self.wynagrodzenie_brutto * 0.015
        skladki_zus_chorobowe = self.wynagrodzenie_brutto * 0.0245
        skladki_ubezpieczenie_zdrowotne = self.wynagrodzenie_brutto * 0.09
        skladki_fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        skladki_fgsp = self.wynagrodzenie_brutto * 0.001
        skladki_fep = self.wynagrodzenie_brutto * 0.015
        koszty = (
            skladki_zus_emerytalne +
            skladki_zus_rentowe +
            skladki_zus_chorobowe +
            skladki_ubezpieczenie_zdrowotne +
            skladki_fundusz_pracy +
            skladki_fgsp +
            skladki_fep
        )
        return koszty

    def oblicz_koszt_pracodawcy(self):
        koszty = self.oblicz_koszty()
        return self.wynagrodzenie_brutto + koszty


def oblicz_koszt_calkowity(nazwa_pliku):
    koszt_calkowity = 0

    with open(nazwa_pliku, 'r', newline='') as plik_csv:
        czytnik = csv.reader(plik_csv)
        next(czytnik)  # Pominięcie nagłówka

        for row in czytnik:
            imie, nazwisko, wynagrodzenie_brutto = row
            pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
            koszt_pracownika = pracownik.oblicz_koszty()
            koszt_calkowity += koszt_pracownika

    return koszt_calkowity


nazwa_pliku = 'pracownicy.csv'
koszt_calkowity = oblicz_koszt_calkowity(nazwa_pliku)
print("Całkowity koszt pracodawcy:", koszt_calkowity)

print("Informacje o pracownikach:")
with open(nazwa_pliku, 'r', newline='') as plik_csv:
    czytnik = csv.reader(plik_csv)
    next(czytnik)  # Pominięcie nagłówka

    for row in czytnik:
        imie, nazwisko, wynagrodzenie_brutto = row
        pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
        koszt_pracownika = pracownik.oblicz_koszty()
        koszt_pracodawcy = pracownik.oblicz_koszt_pracodawcy()
        wynagrodzenie_netto = pracownik.oblicz_wynagrodzenie_netto()

        print("Pracownik:")
        print("- Imię:", imie)
        print("- Nazwisko:", nazwisko)
        print("- Wynagrodzenie brutto:", wynagrodzenie_brutto)
        print("- Koszt pracownika:", koszt_pracownika)
        print("- Koszt pracodawcy:", koszt_pracodawcy)
        print("- Wynagrodzenie netto:", wynagrodzenie_netto)
        print()

suma_kosztow = oblicz_koszt_calkowity(nazwa_pliku)
print("Suma kosztów wynosi:", suma_kosztow)
