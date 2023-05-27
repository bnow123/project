# FUNKCJA SUM_LIST
# function sum_list l -> funkcja, która rekursywnie dodaje elementy
# Czy lista l jest pusta? Yes->0 No-> [0] + the rest -> sum_list(rest)
# przykład list[1,2,3] ->the list is not empty,
# so 1+f[2,3] ->the list is not empty so 2+f[3]->
# the list is not empty so 3+ []->
# the list is empty so return 0
def sum_list(lista):
    if len(lista) == 0:
        return 0
    else:
        data = lista[0]
        lista.pop(0)
        return data + sum_list(lista)

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
# sudoku 4 x 4
# wypełniamy diagram 4 × 4 w taki sposób, aby w każdym wierszu,
# w każdej kolumnie tego kwadratu 4 x 4,
#  znalazło się po jednej cyfrze od 1 do 4 ( w zwykłym sudoku jest od 1 do 9,
#  tu ze względu na mniejszą ilość pól zmniejszamy do 4),
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
# nie wystąpiła już w tym samym wierszu(z wyjątkiem tej aktualnej), kolumny, kwadratu 4 x 4
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

    # Próbuje wypełnić pole liczbami od 1 do 4
    for num in range(1, 5):
        if is_valid(board, row, col, num):
            # Jeśli num może być wstawione, wypełnij pole
            board[row][col] = num

            # jeśli rozwiązanie jest możliwe,no to kończymy:
            if solve_sudoku(board) == "Done":
                return "Done"

            # Jeśli rozwiązanie jest niewłaściwe, cofnij i spróbuj inną liczbę
            board[row][col] = 0

    # Jeśli żadna liczba nie pasuje, zwróć False
    return False


def is_sudoku_solved(board):
    # Sprawdza, czy plansza jest już rozwiązana poprawnie
    # Sprawdzamy, czy w każdym wierszu, kolumnie i bloku 2x2 nie ma powtórzeń
    # oraz czy nie ma żadnych pustych pól (wartości 0)

    # Sprawdź wiersze
    for row in board:
        if sorted(row) != list(range(1, 5)):
            return False

    # Sprawdź kolumny
    for col in range(4):
        column_values = [board[row][col] for row in range(4)]
        if sorted(column_values) != list(range(1, 5)):
            return False

    # Sprawdź bloki 2x2
    # Zastosowano +2 dla block_row i block_col, ponieważ pętla
    # iteruje po blokach 2x2 w planszy 4x4, a każdy blok składa się z 2 wierszy i 2 kolumn.
    # Wartości block_row i block_col też są: 0 i 2, ponieważ wiersze bloków zaczynają się od 0 i 2.
    # Dzięki temu, dla każdego bloku 2x2,
    # wewnętrzne pętle row iterują od block_row do block_row + 2
    # (czyli od 0 do 2 lub od 2 do 4)
    # i col iterują od block_col do block_col + 2
    # (czyli od 0 do 2 lub od 2 do 4).
    # +2 jest używane, aby zdefiniować zakresy
    # wierszy i kolumn dla bloków 2x2 w planszy 4x4.
    for block_row in range(0, 4, 2):
        for block_col in range(0, 4, 2):
            block_values = []
            for row in range(block_row, block_row + 2):
                for col in range(block_col, block_col + 2):
                    block_values.append(board[row][col])
            # Sprawdzamy, czy block_values,
            # czyli lista wartości w danym bloku 2x2, jest różna od listy [1, 2, 3, 4].
            # czyli sprawdzamy w bloku 2x2 nie ma powtórzeń liczb od 1 do 4.
            if sorted(block_values) != list(range(1, 5)):
                return False

    return True


def is_valid(board, row, col, num):
    # Sprawdź, czy wstawienie liczby num do pola (row, col) jest prawidłowe
    # Sprawdzamy, czy num nie występuje już w tym samym wierszu, kolumnie i bloku 2x2

    # Sprawdź wiersz
    if num in board[row]:
        return False

    # Sprawdź kolumnę
    for r in range(4):
        if board[r][col] == num:
            return False

    # Sprawdź blok 2x2
    block_row = (row // 2) * 2
    block_col = (col // 2) * 2
    for r in range(block_row, block_row + 2):
        for c in range(block_col, block_col + 2):
            if board[r][c] == num:
                return False

    return True


def find_empty_cell(board):
    # Znajduje pierwsze wolne pole w planszy i zwraca jego współrzędne (row, col)
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return row, col
    return None


# sudoku 9 x 9
# wypełnienie diagramu 9 × 9 w taki sposób, aby w każdym wierszu,
# w każdej kolumnie i w każdym z dziewięciu kwadratów
# 3 × 3 znalazło się po jednej cyfrze od 1 do 9.
# dla każdej komórki przypisany jest numer wiersza i numer kolumny ( row_, col_)
# sudoku oznaczamy jako tablicę, w której niektóre pola są wypełnione dlatego chcemy,
# żeby nasza funkcja szukała pustą komórkę w tablicy, ponieważ to te pola wypełniamy
# jeśli nie ma już pustych komórek to zwraca wartość "Done", co znaczy, że Sudoku zostało rozwiązane
# aby odnaleźć pusta komórkę definiujemy nową funkcje find_empty_cell_2
# jak już znajdzie pustą komórkę określoną współrzędnymi row_, col_ to sprawdza za pomocą funkcji is_valid2,
# która sprawdza poprawność wstawienia liczby do danej komórki
# Przyjmuje ona cztery argumenty:
# `board_` (plansza Sudoku),
# `row_` (indeks wiersza),
# `col_` (indeks kolumny)
# oraz `num_` (liczba do sprawdzenia).
# funkcja ta sprawdzaa czy dana liczba num może być w danej komórce sprawdza czy
# nie wystąpiła już w tym samym wierszu(z wyjątkiem tej aktualnej), kolumny, kwadratu 3x3
# Funkcja `is_valid2` sprawdza, czy liczba `num` może zostać umieszczona w danej komórce
# jeśli Tak to zwraca True jeśli nie to zwraca False
# oznaczenie board_[row_][col_] =0 -> przypisanie 0 do danej komórki oznacza, że komórka jest pusta
# komentarze do danych funkcji, tłumaczące ich działanie są poniżej


def solve_sudoku2(board_):
    # Sprawdź, czy plansza jest już rozwiązana
    if is_sudoku_solved2(board_):
        return "Done"

    # Znajdź następne wolne pole do wypełnienia
    row_, col_ = find_empty_cell_2(board_)

    # Próbuje wypełnić pole liczbami od 1 do 9
    for num in range(1, 10):
        if is_valid2(board_, row_, col_, num):
            # Jeśli num może być wstawione, wypełnij pole
            board_[row_][col_] = num

            # Jeśli rozwiązanie jest możliwe to koniec:
            if solve_sudoku2(board_) == "Done":
                return "Done"

            # Jeśli rozwiązanie jest niewłaściwe, cofnij i spróbuj inną liczbę
            board_[row_][col_] = 0

    # Jeśli żadna liczba nie pasuje, zwróć False
    return False


def is_sudoku_solved2(board_):
    # Sprawdź, czy plansza jest już rozwiązana poprawnie
    # Sprawdzamy, czy w każdym wierszu, kolumnie i bloku 3x3 nie ma powtórzeń
    # oraz czy nie ma żadnych pustych pól (wartości 0)

    # Sprawdź wiersze
    for row_ in board_:
        if sorted(row_) != list(range(1, 10)):
            return False

    # Sprawdź kolumny
    for col_ in range(9):
        column_values = [board_[row_][col_] for row_ in range(9)]
        if sorted(column_values) != list(range(1, 10)):
            return False

    # Sprawdź bloki 3x3
    for block_row_ in range(0, 9, 3):
        for block_col_ in range(0, 9, 3):
            block_values = []
            for row_ in range(block_row_, block_row_ + 3):
                for col_ in range(block_col_, block_col_ + 3):
                    block_values.append(board_[row_][col_])
            if sorted(block_values) != list(range(1, 10)):
                return False

    return True


def is_valid2(board_, row_, col_, num_):
    # Sprawdź, czy wstawienie liczby num do pola (row_, col_) jest prawidłowe
    # Sprawdzamy, czy num_ nie występuje już w tym samym wierszu, kolumnie i bloku 3x3

    # Sprawdź wiersz
    if num_ in board_[row_]:
        return False

    # Sprawdź kolumnę
    for r in range(9):
        if board_[r][col_] == num_:
            return False

    # Sprawdź blok 3x3
    block_row_ = (row_ // 3) * 3
    block_col_ = (col_ // 3) * 3
    for r in range(block_row_, block_row_ + 3):
        for c in range(block_col_, block_col_ + 3):
            if board_[r][c] == num_:
                return False

    return True

# W funkcji `find_empty_cell2`,
# nazwa "2" ze wzgledu na uzycie wyzej,
# Zwrócenie wartości (-1, -1) jako wynik,
#  informuje, że nie ma więcej wolnych pól do wypełnienia.
# W przypadku funkcji `solve_sudoku`, jeśli otrzymamy (-1, -1) jako wynik z `find_empty_cell`,
# oznacza to, że cała plansza została wypełniona


def find_empty_cell_2(board_):
    # Znajdź pierwsze wolne pole na planszy
    for row_ in range(9):
        for col_ in range(9):
            if board_[row_][col_] == 0:
                return row_, col_
    return -1, -1

# Testy
# testy dla funkcji sum_list


k = [1, 2, 3, 4, 5]
sum_result = sum_list(k)
print(sum_result)
# test 2 dla tej funkcji
k = [10, 18, 20, 30, 43]
sum_result = sum_list(k)
print(sum_result)
# test dla silni
a = 5
result = silnia(a)
print(result)
# test 2
a = 10
result = silnia(a)
print(result)
# testy dla funkcji find_max
array1 = [3, 9, 2, 6, 5, 1, 8]
max_value = find_max(array1)
print(max_value)
# test 2
array2 = [pow(9, 3), pow(8, 4), pow(3, 2), pow(4, 3)]
max_value = find_max(array2)
print(max_value)

# funkcja ciąg Fibonacciego
m = 10
fib_sequence = fibonacci_recursive(m)
print(fib_sequence)
# test 2
m = 20
fib_sequence = fibonacci_recursive(m)
print(fib_sequence)
# funkcja sudoku
tablica = [
    [0, 0, 0, 8, 0, 0, 0, 0, 9],
    [0, 1, 9, 0, 0, 5, 8, 3, 0],
    [0, 4, 3, 0, 1, 0, 0, 0, 7],
    [4, 0, 0, 1, 5, 0, 0, 0, 3],
    [0, 0, 2, 7, 0, 4, 0, 1, 0],
    [0, 8, 0, 0, 9, 0, 6, 0, 0],
    [0, 7, 0, 0, 0, 6, 3, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 8, 0],
    [9, 0, 4, 5, 0, 0, 0, 0, 1]
]
solve_sudoku2(tablica)
print("Rozwiązanie Sudoku to:")
for wiersz in tablica:
    print(wiersz)
# poprawne rozwiązanie jakie powinno wyjść:
# [2, 5, 6, 8, 3, 7, 1, 4, 9]
# [7, 1, 9, 2, 4, 5, 8, 3, 6]
# [8, 4, 3, 6, 1, 9, 2, 5, 7]
# [4, 6, 7, 1, 5, 8, 9, 2, 3]
# [3, 9, 2, 7, 6, 4, 5, 1, 8]
# [5, 8, 1, 3, 9, 2, 6, 7, 4]
# [1, 7, 8, 4, 2, 6, 3, 9, 5]
# [6, 3, 5, 9, 7, 1, 4, 8, 2]
# [9, 2, 4, 5, 8, 3, 7, 6, 1]

# test 2
tablica = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku2(tablica)
print("Rozwiązanie Sudoku to:")
for wiersz in tablica:
    print(wiersz)
# poprawne rozwiązanie jakie powinno wyjść:
# [5, 3, 4, 6, 7, 8, 9, 1, 2]
# [6, 7, 2, 1, 9, 5, 3, 4, 8]
# [1, 9, 8, 3, 4, 2, 5, 6, 7]
# [8, 5, 9, 7, 6, 1, 4, 2, 3]
# [4, 2, 6, 8, 5, 3, 7, 9, 1]
# [7, 1, 3, 9, 2, 4, 8, 5, 6]
# [9, 6, 1, 5, 3, 7, 2, 8, 4]
# [2, 8, 7, 4, 1, 9, 6, 3, 5]
# [3, 4, 5, 2, 8, 6, 1, 7, 9]
