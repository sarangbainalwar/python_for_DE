# static method is a methos that belogs to a class rathher than any object from that class or instance usually used for genral utility functions

class employee:
    def __init__(self,name,position):
        self.name=name
        self.position = position
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position=["manager","cashier","cook","janitor"]
        return position in valid_position
    
employee1=employee("Eugune","manager")
employee2=employee("squidward","CMO")
employee3=employee("rang","chef")

print(employee.is_valid_position("CMO"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())