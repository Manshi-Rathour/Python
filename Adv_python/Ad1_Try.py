while True:
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("You entered a no. greater than 6")

    except Exception as e:
        print(e)

print("Thanks for using this code")

