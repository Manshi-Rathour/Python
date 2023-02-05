def readfile(filename):
    try:
        with open(filename, 'r')as f:
            print(f.read())
    except FileNotFoundError:
        print(filename + " is not found")


readfile("text1")
readfile("text2")
readfile("text3")
