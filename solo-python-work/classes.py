import math


class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a + self.b + self.c


moj_troj = Trojkat(5, 4, 3, 5.3)
print(moj_troj.obwod())
class Kolo:
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2 * self.r * math.pi

    def pole(self):
        return math.pi * self.r**2


moje_kolo = Kolo(10)
print(moje_kolo.pole())
print(moje_kolo.obwod())


class Kwadrat:
    def __init__(self, a):
        self.a = a

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a * self.a


moj_kwadrat = Kwadrat(9)
print("Mój kwadrat ma pole: " + str(moj_kwadrat.pole()) + ", a jego obwod to: " + str(moj_kwadrat.obwod()))

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * self.a + 2 * self.b


moj_prosto = Prostokat(4, 8)
print("Mój prostokat ma pole: " + str(moj_prosto.pole()) + ", a jego obwod to: " + str(moj_prosto.obwod()))


class Trapez:
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def pole(self):
        return (self.a * self.h)/2

    def obwod(self):
        return self.a + self.b + self.c + self.d


moj_trapez = Trapez(1, 2, 5, 4, 8)
print("Mój trapez ma pole " + str(moj_trapez.pole()) + ", a jego obwod to " + str(moj_trapez.obwod()))


