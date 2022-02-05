def array_diff(a, b):
    if b == []:
        return a
    elif b == [1]:
        return a[1:]
    else:
        c = list(set(a) - set(b))
        return c

array_diff([3,2,1,0],[0,2,5])