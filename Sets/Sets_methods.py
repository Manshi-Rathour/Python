# creating an empty set
a = set()
print(type(a))
# adding values to an empty set
a.add(4)
a.add(4)
a.add(5)                  # adding value repeatedly does not change a set
a.add(5)
a.add(5)
a.add((4, 5, 6, 7))       # a set can add another set
# a.add({4 : 5})          # a set cannot add list or dict
print(a)

print(len(a))             # prints the length of the set

# removal of an item
a.remove(5)               # removes 5 from the set
# a.remove(15)              # throws an error because 15 is not present in the set
print(a)
