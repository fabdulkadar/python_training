#Finding max value among 3 values using lambda function
max_val = lambda x,y,z: max(x,y,z)
print(max_val(2,4,6))

#Fibonacci Series using recursion function
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter limit for Fibonacci Series : "))
for i in range(n):
    print(fibonacci(i))