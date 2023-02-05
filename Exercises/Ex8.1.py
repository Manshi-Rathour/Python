def greatest(a, b, c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

d = greatest(9, 3, 10)
print(d)