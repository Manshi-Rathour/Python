a = [2, 3, 4, 7, 8, 20, 38, 19, 35]

# b = []
# for item in a:
#     if item % 2 == 0:
#         b.append(item)
# print(b)

b = [i for i in a if i % 2 == 0]
print(b)

