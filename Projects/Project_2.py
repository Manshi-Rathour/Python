import random

randNo = random.randint(1, 10)

userGuess = None
guesses = 0
while userGuess != randNo:
    userGuess = int(input("Enter your guess :"))
    guesses = guesses + 1
    if userGuess == randNo:
        print("You guessed it correct!")
    else:
        if userGuess > randNo:
            print("Lower no. please!")
        elif userGuess < randNo:
            print("Higher no please!")

print("You guessed the no. in "+str(guesses)+" guesses")

with open("hiscore", 'r')as f:
    hiscore = int(f.read())
if hiscore > guesses:
    with open("hiscore", 'w')as f:
        f.write(str(guesses))














