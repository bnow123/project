# FUNKCJA SUM_LIST
# function sum_list l -> funkcja, która rekursywnie dodaje elementy
# Czy lista l jest pusta? Yes->0 No-> [0] + the rest -> sum_list(rest)
# przykład list[1,2,3] ->the list is not empty,
# so 1+f[2,3] ->the list is not empty so 2+f[3]->
# the list is not empty so 3+ []->
# the list is empty so return 0
def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        data = l[0]
        l.pop(0)
        return data + sum_list(l)

# FUNKCJA SILNIA
# function n!
# function silnia -> if n == 0 return 1
# because 0! == 1 for n=/=0 n * silnia (n-1)
# example why: n == 5 so silnia(5) = 5 * 4 * 3 * 2 * 1
# we can write it in simple way because silnia(4) = 4 * 3 * 2 * 1, so silnia(5) = 5 * silnia(4)
# so by defining a function "silnia" we check for each n if its 0 or not,
# and if not we count n * silnia(n-1)
# silnia(n-1) works the same way if n-1 =/= 0 we count (n-1)* silnia(n-2) etc.


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


# FIND_MAX
# za pomocą rekursji znajdujemy największą wartość z tablicy, nie korzystamy z wbudowanej funkcji max(),
# funkcja działa w ten sposób, że zakładamy 3 ścieżki:
# pierwsza, jeśli tablica jest pusta no to wartość None, no bo nic tam nie ma
# druga, gdy długość tablicy wynosi 1 no to zwracamy pierwszy element w języku Python oznaczony jako element 0.
# trzecia,
def find_max(array):
    if len(array) == 0:
        return None
    else:
        if len(array) == 1:
            return array[0]
        # znajdź maksymalną wartość
        # w podtablicy bez pierwszego elementu,
        # nie używamy tu pop bo pop usuwa pierwszy element na miejscu,
        # moglibysmy zrbic array.copy().pop(0) kopiując tablicę
        else:
            sub_max = find_max(array[1:])

        return array[0] if array[0] > sub_max else sub_max


# Fibonacci
# ciąg liczb naturalnych, z których każda kolejna liczba jest określona rekurencyjnie,
# czyli jest zależna od poprzednich.
# ciąg liczb fibonacciego zaczyna się od
# 0 i 1 więc musimy założyć, że jeśli użytkownik wpisze 0 lub 1 to też mu coś wyskoczy,
# ciąg fibonacciego nigdy nie zawiera liczb ujemnych,
# więc aby użytkownik wiedział też na przyszłość generujemy mu odpowiedź,
# że NIE MOŻNA ( niekażdy musi wiedzieć na czym ten ciąg polega)
# w przypadku wpisania n == 1 pokaże mu 0 dlatego że zgodnie z ciągiem fibonacciego pierwszy wyraz czyli n=1 wynosi 0.
# n w naszym przypadku to DŁUGOŚĆ CIĄGU FIBONACCIEGO
# dla n == 2 program pokaże 2 pierwsze wyrazu ciągu czyli [0,1]
# dla kolejnych liczb funkcja sumuje 2 poprzednie wyrazy, dlatego wprowadzamy argument sequence,
# który oblicza wartość funkcji dla poprzedniego wyrazu, czyli np.
# jesli n=3 to argument sequence to inaczej obliczona funkcja dla argumentu n-1=2,
# a w warunkach funkcji opisane jest, że w przypadku gdy n=2 to ma zwrócić [0,1]
# argument next_number opisuje kolejną liczbę ciągu której szukamy by stworzyc ciąg fibonacciego o długosci n=3
# by otrzymać ciąg fibonacciego o długości n=3
# (czyli otrzymać kolejną, trzecią liczbę ciągu), sumujemy argumenty sequence
# z tym, że bierzemy dwa poprzednie elementy z listy,
# a skoro 1 element z listy to 0 to poprzedni to będzie -1, później -2 itd.
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:            # elif zamiast else, później if
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        return sequence


