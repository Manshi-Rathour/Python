try:
    a = int(input("Enter a no.: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("please enter a valid value")
except ZeroDivisionError as e:
    print("make sure you are not dividing by 0")

print("Thanks for using this code")
