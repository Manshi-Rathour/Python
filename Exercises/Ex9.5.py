words = ['Mango', 'Apple', 'Banana', 'Watermelon']

with open('Ex9.5', 'r')as f:
    content = f.read()

for word in words:
    content = content.replace(word, '######')
    with open('Ex9.5', 'w')as f:
        f.write(content)
