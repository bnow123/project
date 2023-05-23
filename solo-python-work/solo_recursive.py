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


