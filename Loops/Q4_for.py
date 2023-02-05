for i in range(1, 6):
    print("Are you tired?")
    a = input("yes or no : ")
    if a == "yes":
        print("You didn't finish the race!")
        break
    elif a == "no":
        continue

if a == "no" and i == 5:
    print("congratulation you have finished the race!")

