a = 54
def func1():
    global a
    print("statement 1: " + str(a))
    a = 8
    print("statement 2: " + str(a))


func1()
print("statement 3: " + str(a))
