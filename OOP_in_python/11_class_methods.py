# class methods = allow operations related to the class itself, take cls as the first parameter which represents the class itself

class student:
    count=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count+=1
        student.total_gpa+=gpa
        
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"average gpa: {cls.total_gpa/cls.count:.2f}"
    
st1=student("rana",3.2)    
st2=student("rana1",3.2)    
st3=student("rana2",3.2)    

print(student.get_count())
print(student.get_average_gpa())