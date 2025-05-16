"""Read an employee data with employee id, Name, job, basicpay based on job calculate the allowances. 
If job is "manager" 5% on basic pay as allowances 
If job is "developer" 8% on basic pay as allowances 
If job is "analyst" 12% on basic pay as allowances 

find payable salary as basicpay + allowances"""

empID = int(input("Enter Employee Id: "))
empName = input("Enter Employee Name: ")
empDes = input("Enter Employee Designation: ")
empBasicPay = int(input("Enter Basic Pay: "))

empAllowancePercentage = 0.05 if empDes =="manager" else 0.08 if empDes =="developer" else 0.012 if empDes =="analyst" else 0 #Allowance Percentage based on job
empAllowance = empBasicPay*empAllowancePercentage #Calculating Allowance
empPayableSalary = empBasicPay+empAllowance #Calculating Payable Salary

print(f"{empName}'s Allowance is {empAllowance} and Payable Salary is {empPayableSalary}") #Display the results