
# """
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# """

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# for item in thistuple:
#     print(item)

# one_item_tuple = ("apple",)

# tuple1 = ("abc", 34, True, 40, "male")

# this_tuple = tuple(("text",1,"txt"))
# print(type(thistuple))

# """
# A tuple can also be created without using parentheses. This is known as tuple packing.
# """

this_is_tuple_also = 1,2,3,4,5,6,7,8
# print(type(this_is_tuple_also))

# for x in range(0,len(this_is_tuple_also)):
#     print(this_is_tuple_also[x])

x = len(this_is_tuple_also)-1
while x > -1:
    print(this_is_tuple_also[x])
    x -= 1

