import random
# Snake Water Gun
def gameWin(comp, you):
# if you and comp will choose same the game will tie
    if comp == you:
        return None
# if comp choose snake
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
# if comp choose water
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
# if comp choose gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
sum = 0
for i in range(10):
    print("comp turn: Snake(s), Water(w) or Gun(g)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'

    you = input("your turn: Snake(s), Water(w) or Gun(g)?")

    a = gameWin(comp, you)

    print("comp choose "+comp)
    print("you choose "+you)


    if a == None:
        print("Game tie!")
    elif a == True:
        print("You win!")
        sum = sum + 1
    else:
        print("You lose!")


print(sum)
f = open('Ex9.2', 'r')
if f.read() < str(sum):

    f = open('Ex9.2', 'w')
    f.write(str(sum))
f.close()


