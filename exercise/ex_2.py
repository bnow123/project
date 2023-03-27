# kwadrat
import math

a = 10
obwod = a * 4
pole = a * a

# Obwod kwadratu wynosi 40, a pole 100.
print("Obwod kwadratu wynosi " + str(obwod) + ", a pole " + str(pole) + ".")

# prostokat

a = 10
b = 2
obwod = a * 2 + b * 2
pole = a * b

print("Obwod prostokata wynosi " + str(obwod) + ",a pole prostokata wynosi " + str(pole) + ".")

# kolo

r = 5
pi = math.pi
obwod = 2 * pi * r
pole = pi * r * 2

print("Obwod kola wynosi "+ str(obwod) + ",a pole kola wynosi " + str(pole) + ".")

# trapez

a = 3
b = 7
c = 5
d = 6
h = 3
obwod = a + b + c + d
pole = ((a + b) * h)/2
print("Obwod trapezu wynosi "+ str(obwod) + ",a pole trapezu wynosi " + str(pole) + ".")