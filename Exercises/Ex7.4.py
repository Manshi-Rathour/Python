n = int(input("enter the no. to check whether it is prime or not : "))
prime = True
for i in range(2, n):
    if n % i == 0 and n != 2:
        prime = False

if prime:
    print("this is prime no.")
else:
    print("this is not a prime")



