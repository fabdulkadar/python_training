'''Implmenting Polymorphism - Duck Typing
    Duck Typing is a concept in programming where the type of class of an object is detemined by the methods and properties
    that the object has rather than the actual type of the object itself'''

class Student:
    def get_role(self):
        print("Student Learns New Skills")

class Trainer:
    def get_role(self):
        print("Trainer teaches New Skills to the Student")

class Admin:
    def get_role(self):
        print("Admin Manages the administration")

def show_role(person):
    person.get_role()

def main():
    print("1: Student\n2: Trainer\n3: Admin\n")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        show_role(Student())
    elif choice == 2:
        show_role(Trainer())
    elif choice == 3:
        show_role(Admin())

if __name__ == "__main__":
    main()
