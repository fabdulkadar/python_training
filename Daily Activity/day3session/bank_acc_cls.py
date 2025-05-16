''' Inheritance Implementation in Employee Payroll System'''

#Creating Payroll CLass
class Payroll:
    company_name = "Southern Infotech Pvt Ltd"
    def __init__(self, empId, empName, basicPay):
        self.empID = empId
        self.empName = empName
        self.basicPay = basicPay

    def calcualate_hra(self,hra_percentage=0.1):
        return self.basicPay*hra_percentage
    
    def calcualate_pf(self,pf_percentage=0.2):
        return self.basicPay*pf_percentage
    
    def calculate_totalpay(self):
        return self.basicPay+self.calcualate_hra()+self.calcualate_pf()
    
    @staticmethod
    def welcome_message():
        print(f"Welcome to {Payroll.company_name}\n")
    
    def display_payslip(self):
        print("Employee Details")
        print("="*15)
        print(f"Id : {self.empID}")
        print(f"Name : {self.empName}")
        print(f"Basic Pay : {self.basicPay}")
        print(f"HRA : {self.calcualate_hra()}")
        print(f"PF : {self.calcualate_pf()}")
        print(f"Total Pay : {self.calculate_totalpay()}")
        print("-"*30)

#Creating Update Payroll class inheritinh Payroll as super class
class UpdatePayroll(Payroll):
    def __init__(self, empId, empName, basicPay, incr_percentage):
        super().__init__(empId, empName, basicPay)
        self.incr_percentage = incr_percentage 

    def increase_basic_pay(self):
        self.basicPay+=self.basicPay*(self.incr_percentage/100)
        return self.basicPay

    def display_payslip(self):
        print("Employee Details")
        print("="*15)
        print(f"Id : {self.empID}")
        print(f"Name : {self.empName}")
        print(f"Basic Pay : {self.basicPay}")
        print(f"HRA : {self.calcualate_hra()}")
        print(f"PF : {self.calcualate_pf()}")
        print(f"Total Pay After Increment: {self.increase_basic_pay()}")
        print("-"*30)


def main():

    Payroll.welcome_message()

    emp1 = Payroll(101,"John Doe",50000)
    emp2 = Payroll(102,"Bob Smith",75000)
    emp3 = Payroll(103,"Alice Jhonson",85000)
    employees = [emp1, emp2, emp3]

    for emp in employees:
        emp.calcualate_hra()
        emp.calcualate_pf()
        emp.calculate_totalpay()
        emp.display_payslip()

    empl = UpdatePayroll(103,"Alice Jhonson",85000, 15) 
    empl.increase_basic_pay()
    empl.display_payslip()


if __name__ == "__main__" :
    main()

    