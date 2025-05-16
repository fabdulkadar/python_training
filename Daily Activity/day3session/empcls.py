'''Creating a class for performing operations on employee details'''

#Creating the class
class Employee:
    company_name = "Southern Infotech Pvt Ltd"
    
    def __init__(self, emp_name, emp_id, emp_dept, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_dept = emp_dept
        self.emp_salary = emp_salary
    
    #Display Details Method 
    def display_details(self):
        print(f"Company Name : {Employee.company_name}")
        print(f"Employee Name : {self.emp_name}")
        print(f"Employee Id : {self.emp_id}")
        print(f"Employee Department : {self.emp_dept}")
        print(f"Employee Salary : {self.emp_salary}")
        print("-"*30)

    #Method to calculate the annual salary
    def annual_salary(self):
        return self.emp_salary*12
    
    #Method to apply increment in salary
    def apply_increment(self,percentage):
        increment = self.emp_salary*(percentage/100)
        self.emp_salary+=increment

    #Method to check employees earning higher than 70000
    def is_higher_earner(self):
        return self.emp_salary > 70000
    
    #Static Method to display welcome Message
    ''' Static Methods can be called and executed without creating objects '''
    @staticmethod
    def welcome_message():
        print(f"Welcome to {Employee.company_name}\n")

def main():
    emp1 = Employee("John Doe",101,"IT",50000)
    emp2 = Employee("Bob Smith",102,"HR",75000)
    emp3 = Employee("Alice Jhonson",103,"Finance",85000)

    Employee.welcome_message()

    emp1.display_details()
    emp2.display_details()
    emp3.display_details()

    print("Annual Salary Details\n")
    print(f"{emp1.emp_name} : {emp1.annual_salary()}")
    print(f"{emp2.emp_name} : {emp2.annual_salary()}")
    print(f"{emp3.emp_name} : {emp3.annual_salary()}")
    print("-"*30)

    emp1.apply_increment(10)
    emp2.apply_increment(20)
    emp3.apply_increment(30)

    print("Annual Salary Details after Increment\n")
    print(f"{emp1.emp_name} : {emp1.annual_salary()}")
    print(f"{emp2.emp_name} : {emp2.annual_salary()}")
    print(f"{emp3.emp_name} : {emp3.annual_salary()}")
    print("-"*30)

    print(f" Is {emp1.emp_name} a higher earner ? {'Yes' if emp1.is_higher_earner() else 'No'}")
    print(f" Is {emp2.emp_name} a higher earner ? {'Yes' if emp2.is_higher_earner() else 'No'}")
    print(f" Is {emp3.emp_name} a higher earner ? {'Yes' if emp3.is_higher_earner() else 'No'}")

if __name__ == "__main__":
    main()