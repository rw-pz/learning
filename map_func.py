
"""
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
"""


def addition(n):
    return n + n

numbers = (1,2,3,4,5)
result = map(addition,numbers)
print(list(result))

def create_matrix(array_1:list,array_2: list):
    result = map(lambda x,y: x * y, array_1,array_2)
    print(list(result))

create_matrix([2,3,4],[5,6,7])