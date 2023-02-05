a = int(input("Enter a : "))
b = int(input("Enter b : "))
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print('infinite')
