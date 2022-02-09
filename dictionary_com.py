
square = {num: num*num for num in range(1,11)}
print(square)

"""
dictionary = {key: value for vars in iterable}
"""

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.74

# items() method is used to return the list with all dictionary keys with values.
 
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

print(old_price.items())

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k:v for (k,v) in original_dict.items() if k[0] == "j"}
print(even_dict)