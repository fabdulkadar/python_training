''' 
    '''

#User Defined Function for to find is the number is perfect or not
def is_perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    else:
        return False


#Calling the function from main function

if __name__ == "__main__":
    num= int(input("Enter Number : "))
    if is_perfect_number(num):
        print(f"{num} is a Perfect Number")
    else :
        print(f"{num} is not a Perfect Number")
