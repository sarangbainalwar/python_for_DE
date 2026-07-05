class Animal:
    
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"this {self.name} animal is eating")
        
    def sleep(self):
        print(f"this {self.name} animal is sleeping")

class prey(Animal):
    def flee(self):
        print(f"this {self.name} is a prey class")

class predator(Animal):
    def hunt(self):
        print(f"this {self.name} animal is hunting")

class rabbit(prey):
    pass

class hawk(predator):
    pass

class fish(prey,predator):
    pass

rabbit=rabbit("bugs")
hawk=hawk("hawk")
fish=fish("nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()