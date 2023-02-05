class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print("Name is "+self.name)
        print("Train is "+self.train)


harryApplication = RailwayForm()
harryApplication.name = "Harry"
harryApplication.train = "Rajdhani Express"

harryApplication.printData()
