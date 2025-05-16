#Writing Data to a file
def write_emp_data(record):
    with open ("employees.txt","w") as file:
        file.write("ID,Name,Department,Salary\n")
        file.write(record)    

#Reading Employee Data
def read_emp_data():
    try:
        with open("employees.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File Not Found Error")

#Appending data to file
def append_emp_data(record):
    with open ('employees.txt',"a", newline='\n') as file:
        file.write(record) 

