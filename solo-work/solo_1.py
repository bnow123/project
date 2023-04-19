# zadanie 1.1

hello = "Hello"
student = "Beata"
print("{} {}".format(hello, student))

# zadanie 1.2

student_name = input("Wpisz swoje imię:")
print("{} {}".format(hello, student_name))

# zadanie 1.3

students = ["Bajka", "Bójka", "Brawurka", "Mojojojo"]
liczba_studentow = len(students)
print("Liczba studentów wynosi: {} ".format(liczba_studentow))
# zadanie 1.4

for i in range(4):
    print("Hello ", students[i])

# zadanie 1.5

liczba = 5
potega = 3

wynik = liczba ** potega
# oczekiwany rezultat:
# Wynik wynosi: 125
print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')
# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: {}".format(liczba_nawiasow_otwierajacych))

# zadanie 1.7

students = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
students_sorted = sorted(students)
print("Alfabetyczna lista studentow:")
for i in range(len(students)):
    print(students_sorted[i])

# zadanie 1.8

students_surnamesorted = sorted(students, key=lambda x: x.split(" ")[-1])
print("Alfabetyczna lista studentow wg nazwiska:")
for i in range(len(students)):
    print(students_surnamesorted[i])

# zadanie 1.9

students = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = len([element for element in students if "N" in element])
print("Liczba osob, ktorych nazwiska zaczynaja sie na N: ", liczba_n)

# zadanie 1.10


def wektory(list_a, list_b):
    result = []
    for item_a, item_b in zip(list_a, list_b):
        result.append(item_b - item_a)
    return result


def rownosc_wektorow(list_a, list_b):
    result = True
    for item_a, item_b in zip(list_a, list_b):
        if item_a != item_b:
            result = False
    return result


wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = rownosc_wektorow(wektory(wykres_1[0], wykres_1[1]), wektory(wykres_1[1], wykres_1[2]))
wykres_2_funkcja_liniowa = rownosc_wektorow(wektory(wykres_2[0], wykres_2[1]), wektory(wykres_2[1], wykres_2[2]))
wykres_3_funkcja_liniowa = rownosc_wektorow(wektory(wykres_3[0], wykres_3[1]), wektory(wykres_3[1], wykres_3[2]))

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
