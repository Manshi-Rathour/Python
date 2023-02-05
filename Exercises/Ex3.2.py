letter = '''Dear NAME,
You are selected!
Date : DATE'''

name = input("Enter your name :")
date = input("Enter date :")

letter = letter.replce("NAME", name)
letter = letter.replce("DATE", date)
print(letter)