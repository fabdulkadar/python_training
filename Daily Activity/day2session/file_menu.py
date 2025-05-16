from filehandling import file_handling_menu

try :
    while True:
        print("Welcome to File Handling System")
        print("1: Write to file")
        print("2: Read File")
        print("3. Append File")
        print("4. Exit")
        choice = int(input("Enter the preferred choice : "))
        if choice == 1:
            record=input("Enter Text : ")
            file_handling_menu.write_emp_data(record)
        elif choice == 2:
            file_handling_menu.read_emp_data()
        elif choice == 3:
            record=input("Enter Text to Append : ")
            file_handling_menu.append_emp_data(record)
        elif choice == 4:
            print("Exitting Program...")
            break
        else:
            print("Invalid Choise, Try Again.")
            continue

except ValueError:
    print("Invalid Input, Try Again!")

else :
    print("Program Exited Successfully")

finally:
    print("Thank you for using the File Handling System")