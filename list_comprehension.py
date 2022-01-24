
# # numbers = [1,2,3,4,5]

# # newlist = [number ** 2 for number in numbers]
# # print(newlist)

# # newlist = [number for number in range(10)]
# # print(newlist)

# # letters = []

# # for letter in "human":
# #     letters.append(letter)

# # print(letters)

# # # list comprehension

# # letters = [letter for letter in "human"]
# # print(letters)

# """

# Syntax of List Comprehension

# [expression for item in list]

# list = [expression for item in iterable (if conditional)]

# ==> List comprehensions are relatively faster than for loops.

# """

# # 1

# a = [4,6,7,3,2]

# b = [x for x in a if x > 5]
# print(b)

# # 2

# b = [x*2 for x in a if x > 5]
# print(b)

# # 3

# names = ['Ch','Dh','Eh','cb','Tb','Td']
# new_names = [name for name in names if name.lower().startswith('c')]

# print(new_names)

# # 4

import numpy as np

A = np.random.randint(10, size=(4,4))
print(A)

max_element = [max(i) for i in A]
print(max_element)

# 5

vals = [[1,2,3],[4,5,6],[7,8,9]]
vals_max = [max(x) for x in vals]
print(vals_max)

# 6

names = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']
new_names = [name for name in names if name.lower().endswith('b') and len(name) > 2]
print(new_names)

"""
Generator
"""

def square_numbers(numbers):
    for number in numbers:
        yield (number*number)

my_numbers = square_numbers([1,2,3,4,5])
print(my_numbers)

for my_number in my_numbers:
    print(my_number)

