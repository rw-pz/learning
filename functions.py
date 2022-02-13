
# def my_function(fname):
#     print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

    
# """
# We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
# """

# def names(**kwargs):
#     print(kwargs)

# names(first="John",second="Wick")

# def printing(*args):
#     print(args)

# printing("arg1","arg2")

# def new_func(*args):
#     for arg in args:
#         print(arg, "=>", arg*arg)

# new_func(1,2,3,4,5)

def exponentiation():
    base = int(input("Exponent base: "))
    exponent = int(input("Exponent: "))
    result = base ** exponent
    print(result)

exponentiation()