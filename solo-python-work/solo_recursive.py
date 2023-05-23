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


