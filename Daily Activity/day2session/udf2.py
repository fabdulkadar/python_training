'''default argument will be used if the argument is not passed by the user
    when the arguments are optional defualt value is used'''

def add(x,y=1):
    sum = x+y
    return sum

print(add(4))