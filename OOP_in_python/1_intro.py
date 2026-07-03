from car import car
car1=car("Fronx",2025,"black",False)
car2=car("BMC",2025,"black",True)

print(car1.model)
print(car1.for_sale)
print(car1.year)

car1.stop()
car1.drive()
car2.stop()
car2.drive()
car1.getter()
car2.getter()