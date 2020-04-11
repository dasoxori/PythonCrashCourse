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

myNewCar = Car("audi", "a4", 2016)

print(myNewCar.getDescripteveName())

myNewCar.odometerReading = 23 # modify directly attribute value
myNewCar.updateOdometer(50) # modify attribute value through a method

myNewCar.readOdometer()

myUsedCar = Car("subaru", "outback", 2013)
print ("\n" + myUsedCar.getDescripteveName())

myUsedCar.updateOdometer(23500)
myUsedCar.readOdometer()
myUsedCar.incrementOdometer(100)
myUsedCar.readOdometer()