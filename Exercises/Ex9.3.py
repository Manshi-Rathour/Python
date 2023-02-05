with open('Table', 'w') as f:
    for i in range(2, 21):
        for j in range(1, 11):
            f.write(str(i * j))
            if j !=11:
                f.write('\n')

        f.write('\n')










