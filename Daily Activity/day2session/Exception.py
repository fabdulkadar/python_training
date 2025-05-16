try:
    a = int(input("Enter number : "))
except ValueError:
    print("Please enter a validnumber")
else :
    print("Square of a number : ", a*a)