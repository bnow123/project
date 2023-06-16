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
