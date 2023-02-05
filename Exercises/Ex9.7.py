content = True

i = 1
with open('Ex9.7', 'r')as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print("Yes python is present on line no. "+str(i))
        i = i+1

