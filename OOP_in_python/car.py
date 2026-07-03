class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        
    def drive(self):
        print(f"the car is driving {self.model}")
        
    def stop(self):
        print(f"the car has stopped {self.model}")
        
    def getter(self):
        print(f"the car is {self.model}, color is {self.color}, year is {self.year} and for sale is {self.for_sale}")