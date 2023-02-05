l = [2200, 2350, 2600, 2130, 2190]

print("dollars that spend extra in feb compared to jan is " + str(l[1]-l[0]))
print("total expense in 1st quarter of the year : "+str(l[0]+l[1]+l[2]))
if 2000 in l:
    print("2000 is in list")
else:
    pass
l.append(1980)
print(l)
a = int(l[3])-200
l.remove(2130)
l.insert(3, a)
print(l)


