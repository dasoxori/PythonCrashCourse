# This file has only the class Car, we are going to use it as a Module with just this class
# A class that can be used to represent a car.
class Car():
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescripteveName(self):
        # return a neatly formatted descriptive name.
        longName = str(self.year) + " " + self.make + " " + self.model
        return longName.title()

    def readOdometer(self):
        # print a statement shownig the car's mileage.
        print("This car has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self, mileage):
        # set odometer reading to the given value.
        # reject the change if it attempts to roll the odometer back.
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        # add the given amount to the odometer reading.
        self.odometerReading += miles