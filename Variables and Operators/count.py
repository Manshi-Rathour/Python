li = [1, 2, 3, 1, 2, 3, 10, 1, 1, 2, 1, 8, 3, 10, 10, 3, 1, 1]


count = 0
a = int(input("Enter a no.:"))
li.append(a)

for i in li:
    if i == a:
        count = count + 1

print(count)


