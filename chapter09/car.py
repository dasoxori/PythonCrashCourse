# Working with classes and Instances
"""A class that can be used to represent a car"""

class Car():
    """A simple attempt to represent a car."""
    # The __init__ method runs every time the class runs
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometerReading) + " miles on it")

    def updateOdometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometerReading += miles


# we can connect using super(). method the child with the parent class
# in order to use parrents methods.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        The initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, batterySize = 70):
        """Initialize the battery's attributes."""
        self.batterySize = batterySize
    
    def describeBattery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.batterySize) + "-KWh battery.")

    def getRange(self):
        """Print a statement about the range this battery provides"""
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

