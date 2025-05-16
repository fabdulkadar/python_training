''' Student Management System 
    Add View Update Delete
    using OOPS concept like Classes&Objects, Inheritance, Dunder Function'''

class Student:

    def __init__(self, std_Name, std_Id, std_email, std_phno, std_class):
        self.std_Name = std_Name
        self.std_Id = std_Id
        self.std_email = std_email
        self.std_phno = std_phno
        self.std_class = std_class
        
    def __len__(self):
        return len(self.std_phno)
    
    def __str__(self):
        return f"Student Name : {self.std_Name}\nStudent ID : {self.std_Id}\nStudent Email : {self.std_email}\nStudent Phone No : {self.std_phno}\nStudent Class : {self.std_class}"
    
    

class UpdateStudent(Student):
    students = {}
    def __init__(self, std_Name, std_Id, std_email, std_phno, std_class):
        super().__init__(std_Name, std_Id, std_email, std_phno, std_class)
    
    def view_students(self):
        for id, value in self.students.items():
            print("-"*30)
            print(f"{id} : {value}")
            print("-"*30)

    def add_student(self):
        self.std_Name = input("Enter Name : ")
        self.std_phno = int(input("Enter 10 Digit Phone Number : "))
        self.std_email = input("Enter Email Address : ")
        self.std_class = input("Enter Class : ")
        self.std_Id = int(input("Enter Student Id : "))
        self.students[self.std_Id]={"name":self.std_Name,"phno":self.std_phno,"email":self.std_email,"class":self.std_class}
        print("Record Added Succesfully!")

    def update_student(self):
        try :
            id = int(input("Enter Student Id to update : "))
            if id not in self.students.keys():
                print("Student ID not found")
            else:
                print("Values :")
                print("1. Name\n2. Phone Number\n3. Email\n4. Class")
                choice = int(input("Choose Which Value to edit :"))
                if choice==1:
                    self.std_Name = input("Enter New Name : ")
                    self.students[id]["name"] = self.std_Name
                    print("Name Updated Successfully!")
                elif choice == 2:
                    self.std_phno = int(input("Enter New Phone No : ")) 
                    self.students[id]["phno"] = self.std_phno
                    print("Phone Number Updated Successfully!")
                elif choice == 3:
                    self.std_email = input("Enter New Email : ") 
                    self.students[id]["email"] = self.std_email
                    print("Email Updated Successfully!")
                elif choice == 4:
                    self.std_class = input("Enter New Class : ") 
                    self.students[id]["class"] = self.std_class
                    print("Class Updated Successfully!")         
        except ValueError :
            print("Invalid Input, Try Again")

    def delete_student(self):
        try :
            id = int(input("Enter Student Id to be deleted : "))
            if id not in self.students.keys():
                print("Student ID not found")
            else: 
                self.students.pop(id)
                print(f"The record for {id} is deleted successfully!")
        except ValueError:
            print("Invalid Input, Try Again")


def main():
    stud = UpdateStudent("", 0, "", "", "")
    stud1 = Student("John", 101, "john@gmail.com", "6984569874", "CSEA")
    while True:
        print("1. View\n2. Add\n3. Update\n4. Delete\n5. Exit")
        choice = int(input("Choose Action :"))
        if choice==1:
            stud.view_students()
        elif choice == 2:
            stud.add_student()
        elif choice == 3:
            stud.update_student()
        elif choice == 4:
            stud.delete_student()
        elif choice == 5:
            print("Exiting the program")
            break
        else:
            print("Invalid Input, Try Again")   
            continue
    print(f"Phone number has '{len(stud1)}' digits")
    print(stud1)
           
if __name__ == "__main__":
    main()
