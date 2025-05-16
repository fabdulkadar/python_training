from arithmetic import basic_ops, advanced_op

while True:
    print("***===Calculator===***")
    print("===Basic Operations===")
    print("1: Add")
    print("2: Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("===Advanced Operations===")
    print("5: Square")
    print("6: Square Root")
    print("7: Exit Application")

    choice = int(input("Enter the preffered choice : "))
    if choice == 1:
        arg1=int(input("Enter 1st Operand"))
        arg2=int(input("Enter 2nd Operand"))
        print(basic_ops.add(arg1,arg2))
    elif choice == 2:
        arg1=int(input("Enter 1st Operand"))
        arg2=int(input("Enter 2nd Operand"))
        print(basic_ops.sub(arg1,arg2))
    elif choice == 3:
        arg1=int(input("Enter 1st Operand"))
        arg2=int(input("Enter 2nd Operand"))
        print(basic_ops.mul(arg1,arg2))
    elif choice == 4:
        arg1=int(input("Enter 1st Operand"))
        arg2=int(input("Enter 2nd Operand"))
        print(basic_ops.divide(arg1,arg2))
    elif choice == 5:
        arg1=int(input("Enter 1st Operand"))
        arg2=int(input("Enter 2nd Operand"))
        print(advanced_op.sqr(arg1,arg2))
    elif choice == 6:
        arg1=int(input("Enter 1st Operand"))
        print(advanced_op.sqrt(arg1))
    elif choice == 7:
        print("Exitting Program...")
        break
    else:
        print("Invalid Choise, Try Again.")
        continue