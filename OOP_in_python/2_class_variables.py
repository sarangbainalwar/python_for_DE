class Student:
    
    class_year = 2025+1
    num_stds=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        Student.num_stds+=1
    
st1=Student("Sarang",23)
st2=Student("Aisle",22)
st3=Student("squid",55)
st4=Student("sandy",55)

print(st1.name)
print(Student.class_year)
print(st2.name)

print(f"my graduating class of {Student.class_year} has {Student.num_stds}")