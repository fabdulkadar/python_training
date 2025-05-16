try :
    numr = int(input("Enter Numerator : "))
    denom = int(input("Enter Denominator : "))

    result = numr / denom

except ZeroDivisionError:
    print("Error : Division by zero is not valid")

except ValueError:
    print("Invalid Input : Enter numerical valuse")

else :
    print(f"Result: {result}")
    
finally:
    print("Execution Completed Successfully!")