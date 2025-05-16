#Writing Data to a file

with open ("employees.txt","w") as file:
    file.write("ID,Name,Department,Salary\n")
    file.write("101, John Doe, IT, 60000\n")
    file.write("102, Jake Smith, Finance, 55000\n")
    file.write("103, EMily Jhonson, HR, 706000\n")

#Reading Employee Data
try:
    with open("employees.txt","r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File Not Found Error")

#Appending data to file
with open ('employees.txt',"a") as file:
    file.write("104,Michael Brown, MArketing, 62000\n")

#Reading Employee Data
try:
    with open("employees.txt","r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File Not Found Error")

print("New Employee added succesfully")

#Handling exceptions in file handling
try:
    with open("non_existant_file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error : This file doesnt exist")