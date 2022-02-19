
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def check_even(number: int)-> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# # Extract elements from the numbers list for which check_even() returns True
# even_numbers_iterator = filter(check_even, numbers)

# # converting to list
# even_numbers = list(even_numbers_iterator)

# print(even_numbers)

# filter syntax

"""
filter(function, sequence)

Parameters:

function: function that tests if each element of a 
sequence true or not.

sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.

Returns:

returns an iterator that is already filtered.
"""

def fun(variable: str)-> bool:
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False

# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun,sequence)

print("Filtered numbers are:")
for num in filtered:
    print(num)