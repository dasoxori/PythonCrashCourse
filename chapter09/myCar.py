from car import Car

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