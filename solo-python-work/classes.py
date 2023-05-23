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
