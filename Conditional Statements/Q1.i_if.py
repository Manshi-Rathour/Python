india = ["Mumbai", "Banglore", "Chennai", "Delhi"]
pakistan = ["Lahore", "Karanchi", "Islamabad"]
bangladesh = ["Dhaka", "Khulna", "Rangpur"]

c = input("Enter city name: ")

if c in india:
    print("The city belongs to india.")
elif c in pakistan:
    print("The city belong to pakistan.")
else:
    print("The city belong to bangladesh.")
