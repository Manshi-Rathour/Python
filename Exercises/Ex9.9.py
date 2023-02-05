with open('Ex9.8', 'r')as f:
    content1 = f.read()

with open('Ex9.9', 'r')as f:
    content2 = f.read()

if content1 == content2:
    print("Files are identical.")
else:
    print("Files are not identical.")
