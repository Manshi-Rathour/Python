with open('Ex9.4', 'r')as f:
    content = f.read()

content = content.replace('donkey', '######')

with open('Ex9.4', 'w')as f:
    f.write(content)
