india = ["Mumbai", "Banglore", "Chennai", "Delhi"]
pakistan = ["Lahore", "Karanchi", "Islamabad"]
bangladesh = ["Dhaka", "Khulna", "Rangpur"]

a = input("Enter city name: ")
b = input("Enter city name: ")

if (a and b) in india:
    print("Both cities are in india.")
elif (a and b) in pakistan:
    print("Both cities are in pakistan.")
elif (a and b) in bangladesh:
    print("Both cities are in bangladesh.")
else:
    print("They do not belong to same country.")
