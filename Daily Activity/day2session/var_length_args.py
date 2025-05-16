''' var length args'''

#n number of arguments for the function *args
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5))

# Variable Keyword Arguements **kwargs
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}:{value}")

show_profile(name="Fadhil", age=21)
show_profile(name="Fadhil", age=21, height=180)

'''
    Building Blocks of python are : Functions Classes Packages and Modules
'''