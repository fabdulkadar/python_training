class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"{self.name} scored {self.marks} marks"
    
    def __len__(self):
        return len(self.name)
    
    def __add__(self,other):
        return self.marks + other.marks
    
S1 = Student("Anirudh", 85)
S2 = Student("Keerthi", 90)

print(S1) #__str__
print(len(S1)) #__len__
print((S1+S2)/2)