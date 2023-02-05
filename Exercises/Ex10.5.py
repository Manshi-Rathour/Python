class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("**************")
        print("Name of the train is "+self.name)
        print("No. of seats available is "+self.seats)
        print("**************")

    def fareInfo(self):
        print("Fare of a ticket is Rs "+self.fare)

    def bookTicket(self):
        if self.seats > str(0):
            print("Your ticket has been booked. Your seat no. is "+self.seats)
            self.seats = str(int(self.seats) - 1)
        else:
            print("Sorry train is full. Kindly try in tatkal!")


intercity = Train("Intercity Express: 102783", "100", "50")
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()

