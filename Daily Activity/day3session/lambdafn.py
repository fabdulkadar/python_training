add = lambda x,y : x+y
print(f"Sum is : {add(4,2)}")

employees = [
    {"name":"Smith", "salary":50000},
    {"name":"Allen", "salary":60000},
    {"name":"Joe", "salary":45000}
]

sorted_employees = sorted(employees, key=lambda x: x["name"])

for emp in sorted_employees:
    print(emp)