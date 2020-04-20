from car import ElectricCar

myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.getDescriptiveName())
myTesla.battery.describeBattery()
myTesla.battery.getRange()