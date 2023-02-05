class Animals:
    animalType = "Mammal"

class Pets(Animals):
    colour = "White"

class Dog(Pets):
    @staticmethod
    def Bark():
        print("dog barks!")


d = Dog()
d.Bark()
print(d.animalType)
print(d.colour)
