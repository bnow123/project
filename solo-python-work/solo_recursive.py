# function sum_list l -> function which add elements recursively
# is l empty? Yes->0 No-> [0] + the rest -> sum_list(rest)
# example list[1,2,3] ->the list is not empty,
# so 1+f[2,3] ->the list is not empty so 2+f[3]->
# the list is not empty so 3+ []->
# the list is empty so return 0
def sum_list(l):
    if not l:
        return 0
    else:
        return l[0] + sum_list(l[1:])


# Test
l = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum_list(l)
print(result)

# function n!


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


# Test
number = 5
result = silnia(number)
print(result)
# find_max
def find_max(list2):
    if len(list2) == 1:
        return list2[0]
    else:
        return max(list2[0], find_max(list2[1:]))

# Test
list2 = [4, 2, 9, 7, 5]
result = find_max(list2)
print(result)

# Fibonacci