# FUNKCJA SUM_LIST
# function sum_list l -> function which add elements recursively
# is l empty? Yes->0 No-> [0] + the rest -> sum_list(rest)
# example list[1,2,3] ->the list is not empty,
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
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        return sequence

# sudoku
# wypełnienie diagramu 9 × 9 w taki sposób, aby w każdym wierszu,
# w każdej kolumnie i w każdym z dziewięciu kwadratów
# 3 × 3 znalazło się po jednej cyfrze od 1 do 9.
# dla każdej komórki przypisany jest numer wiersza i numer kolumny ( row, col)
# sudoku oznaczamy jako tablicę, w której niektóre pola są wypełnione dlatego chcemy,
# żeby nasza funkcja szukała pustą komórkę w tablicy, ponieważ to te pola wypełniamy
# jeśli nie ma już pustych komórek to zwraca wartość "Done", co znaczy, że Sudoku zostało rozwiązane
# aby odnaleźć pusta komórkę definiujemy nową funkcje find_empty_cell
# jak już znajdzie pustą komórkę określoną współrzędnymi row, col to sprawdza za pomocą funkcji is_valid,
# która sprawdza poprawność wstawienia liczby do danej komórki
# Przyjmuje ona cztery argumenty:
# `board` (plansza Sudoku),
# `row` (indeks wiersza),
# `col` (indeks kolumny)
# oraz `num` (liczba do sprawdzenia).
# funkcja ta sprawdzaa czy dana liczba num może być w danej komórce sprawdza czy
# nie wystąpiła już w tym samym wierszu(z wyjątkiem tej aktualnej), kolumny, kwadratu 3x3
# Funkcja `is_valid` sprawdza, czy liczba `num` może zostać umieszczona w danej komórce
# jeśli Tak to zwraca True jeśli nie to zwraca False
# oznaczenie board[row][col] =0 -> przypisanie 0 do danej komórki oznacza, że komórka jest pusta
# komentarze do danych funkcji, tłumaczące ich działanie są poniżej


def solve_sudoku(board):
    # Sprawdź, czy plansza jest już rozwiązana
    if is_sudoku_solved(board):
        return "Done"

    # Znajdź następne wolne pole do wypełnienia
    row, col = find_empty_cell(board)

    # Próbuje wypełnić pole liczbami od 1 do 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Jeśli num może być wstawione, wypełnij pole
            board[row][col] = num

            # Kontynuuj rekurencyjnie, jeśli rozwiązanie jest możliwe
            if solve_sudoku(board):
                return True

            # Jeśli rozwiązanie jest niewłaściwe, cofnij i spróbuj inną liczbę, czyli dajemy narazie 0 bo pusta komórka
            board[row][col] = 0

    # Jeśli żadna liczba nie pasuje, wróć do poprzedniego poziomu rekurencji, czyli zakładamy,
    # że możemy się pomylić i wtedy wracamy krok wstecz
    return False


def is_sudoku_solved(board):
    # Sprawdź, czy plansza jest już rozwiązana poprawnie
    # Sprawdzamy, czy w każdym wierszu, kolumnie i bloku 3x3 nie ma powtórzeń
    # oraz czy nie ma żadnych pustych pól (wartości 0)

    # Sprawdź wiersze
    for row in board:
        if sorted(row) != list(range(1, 10)):
            return False

    # Sprawdź kolumny
    for col in range(9):
        column_values = [board[row][col] for row in range(9)]
        if sorted(column_values) != list(range(1, 10)):
            return False

    # Sprawdź bloki 3x3
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block_values = []
            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    block_values.append(board[row][col])
            if sorted(block_values) != list(range(1, 10)):
                return False

    return True


def is_valid(board, row, col, num):
    # Sprawdź, czy wstawienie liczby num do pola (row, col) jest prawidłowe
    # Sprawdzamy, czy num nie występuje już w tym samym wierszu, kolumnie i bloku 3x3

    # Sprawdź wiersz
    if num in board[row]:
        return False

    # Sprawdź kolumnę
    for r in range(9):
        if board[r][col] == num:
            return False

    # Sprawdź blok 3x3
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3
    for r in range(block_row, block_row + 3):
        for c in range(block_col, block_col + 3):
            if board[r][c] == num:
                return False

    return True

# W funkcji `find_empty_cell`,
# Zwrócenie wartości (-1, -1) jako wynik,
#  informuje, że nie ma więcej wolnych pól do wypełnienia.
# W przypadku funkcji `solve_sudoku`, jeśli otrzymamy (-1, -1) jako wynik z `find_empty_cell`,
# oznacza to, że cała plansza została wypełniona


def find_empty_cell(board):
    # Znajdź pierwsze wolne pole na planszy
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1


# Testy
# funkcja sum_list
l = [1, 2, 3, 4, 5]
sum_result = sum_list(l)
print (sum_result)
# test 2 dla tej funkcji
k = [10, 18, 20, 30, 43]
sum_result = sum_list(k)
print(sum_result)
# test dla silni
n = 5
result = silnia(n)
print(result)
# test 2
n = 10
result = silnia(n)
print(result)
# funkcja find_max
array = [3, 9, 2, 6, 5, 1, 8]
max_value = find_max(array)
print(max_value)
# test 2
array = [ pow(9, 3), pow(8, 4), pow(3, 2), pow(4, 3)]
max_value = find_max(array)
print(max_value)
