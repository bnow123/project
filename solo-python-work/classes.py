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


class Student:
    def __init__(self, imie, nazwisko, index):
        self.imie = imie
        self.nazwisko = nazwisko
        self.index = index
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.index}"

    def __int__(self):
        return 6

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)


student_Beata = Student("Beata", "Nowicka", 121583)


student_Beata.dodaj_ocene(4)
print(student_Beata)
print(student_Beata.zwroc_srednia())

# class dla Pizzy- zawiera 9 zmiennych


class Pizza:
    def __init__(self, size, crust_type, toppings,
                 cheese_type, sauce_type, extra_cheese,
                 extra_toppings, delivery_address, special_instructions):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings
        self.cheese_type = cheese_type
        self.sauce_type = sauce_type
        self.extra_cheese = extra_cheese
        self.extra_toppings = extra_toppings
        self.delivery_address = delivery_address
        self.special_instructions = special_instructions

    def __str__(self):
        toppings_str = ', '.join(self.toppings)
        extra_toppings_str = ', '.join(self.extra_toppings)
        extra_cheese_str = "Yes" if self.extra_cheese else "No"

        pizza_info = f"""
        Size: {self.size}
        Crust Type: {self.crust_type}
        Toppings: {toppings_str}
        Cheese Type: {self.cheese_type}
        Sauce Type: {self.sauce_type}
        Extra Cheese: {extra_cheese_str}
        Extra Toppings: {extra_toppings_str}
        Delivery Address: {self.delivery_address}
        Special Instructions: {self.special_instructions}
        """

        return pizza_info.strip()

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_price(self):
        base_price = 10  # Base price for a small pizza
        if self.size == "Medium":
            base_price = 12
        elif self.size == "Large":
            base_price = 14

        total_price = base_price

        if self.extra_cheese:
            total_price += 2

        total_price += len(self.extra_toppings) * 1.5

        return total_price


# Test
pizza = Pizza("Large", "Thin Crust",
              ["Pieczarki", "Pepperoni"], "Ser Mozzarella", "Pomidor",
              False, ["Oliwki"], "Najlepsza ulica 6/5",
              "Zostaw przed drzwiami")
pizza.add_topping("Onions")
price = pizza.calculate_price()

print(pizza)
print("Price:", price)
