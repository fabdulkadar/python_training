''' Module that contains Basic Arithmetic Operations like Add, Sub, Multiply and Divide'''

def add(*args):
    return sum(args)

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else :
        print("Invalid! Division by Zero")
