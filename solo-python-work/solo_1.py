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
# oczekiwany rezultat
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
for i in range(len(students)):
    print(students_sorted[i])

# zadanie 1.8

students_surnamesorted = sorted(students, key=lambda x: x.split(" ")[-1])
print("Alfabetyczna lista studentow wg nazwiska:")
# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
for i in range(len(students)):
    print(students_surnamesorted[i])

# zadanie 1.9

students = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = len([element for element in students if "N" in element])
print("Liczba osob, ktorych nazwiska zaczynaja sie na N: ", liczba_n)