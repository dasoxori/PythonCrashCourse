# Creating the dog class

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def rollOver(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

myDog = Dog('willie', 6)
yourDog = Dog('lucy', 3)
print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old.")
myDog.sit() # calling Methods

print("\nYour dog's name is " + yourDog.name.title() + ".")
print("Your dog is " + str(yourDog.age) + " years old.")
yourDog.sit() # calling Methods