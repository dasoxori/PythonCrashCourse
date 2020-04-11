class Dog():

    """A simple attempt to model a dog."""

    # the __init__ methods runs automatically whenever we call the class.
    def __init__(self, name, age): 
        """Initialize name and age attributes."""
        self.name = name # any variable prefixed with self is availible to every method in the class.
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting")

    def rollOver(self):
        """Sumulate rolling over in responce to a command."""
        print(self.name.title() + " rolled over!")

myDog = Dog("fifi", 3)
yourDog = Dog("Lucy", 6)

print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " +str(myDog.age) + " years old.")
myDog.sit()

print("\nYour dog's name is " + yourDog.name.title() + ".")
print("Your dog is " + str(yourDog.age) + " years old.")
yourDog.sit()