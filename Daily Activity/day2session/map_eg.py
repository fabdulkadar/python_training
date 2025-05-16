from functools import reduce
#List - Map, Reduce, Filter
marks = [65,84,50,35,98,76,85]

grades = list(map(lambda x : 'A' if x>90 and x<=100 else 'B' if x>80 and x<=90 else 'C' if x>70 and x<=80 else 'D' if x>60 and x<70 else 'F' , marks))
print(f"Grades for the marks :\n{marks}\n{grades}")

filtered_marks = list(filter(lambda x : x>80,marks))
print(f"Marks Above 80 : {filtered_marks}")

total_marks = reduce(lambda x,y: x+y, marks)
print(f"Total Marks : {total_marks}")

#Set - Map, Reduce, Filter
names = {"John","Joe","Smith","Bob"}
set_3 = set(map(lambda x: x[0:3], names))
print("-"*50,"\n",set_3)

set_4 = set(filter(lambda x: len(x) == 4,names ))
print("-"*50,"\n",set_4)

set_5 = reduce(lambda x,y: x+y, names)
print("-"*50,"\n",set_5)

#Tuple - Map, Reduce, Filter
names = ("John","Joe","Smith","Bob")
tuple_3 = tuple(map(lambda x: x[0:3], names))
print("-"*50,"\n",tuple_3)

tuple_4 = tuple(filter(lambda x: len(x) == 4,names ))
print(tuple_4)

tuple_5 = reduce(lambda x,y: x+y, names)
print(tuple_5)

#Dictionary - Map, Reduce, Filter
names = {"John": 1,"Joe": 2,"Smith": 3,"Bob": 4}    
dict_3 = dict(map(lambda x: (x[0][0:3],x[1]), names.items()))
print("-"*50,"\n","First Three letters of all keys : ",dict_3)

dict_4 = dict(filter(lambda x: len(x[0]) == 4,names.items() ))
print("Names with 4 letters : ",dict_4)

dict_5 = reduce(lambda x,y: x+y, names.items())
print(dict_5)
