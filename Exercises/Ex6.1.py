a = int(input("first no. : "))
b = int(input("sec no. : "))
c = int(input("third no. : "))
d = int(input("fourth no. : "))
if a > b and a > c and a > d:
    print(a)
elif b > c and b > d:
    print(b)
elif c > d:
    print(c)
else:
    print(d)
