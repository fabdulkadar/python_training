""" Validate the employee email """

#Employee Data
employees = [
    {"name":" Alice Jhonson", "email":"Alice.J@company.com"},
    {"name":"Bob Smith", "email":"bob.smith@company.com"},
    {"name":"Carol Lee", "email":"carol.lee@otherdomain.com"}
]


for emp in employees:
    name = emp["name"].strip() #Remove Extra Spaces
    email = emp["email"].strip().lower()
    email = email.replace(email[email.index("@"):], "@altimetrik.com") #Replace the domain with @altimetrik.com 
    parts = name.lower().split() #Convert to lowercase letters and split the name by space

    #Email Validate
    if not email.startswith(parts[0].lower()): #Check if the first part of the email matches the first name of the employee
        print(f"Invalid Email Format for {name}: Doesn't start with the name")
        continue
    if "@altimetrik.com" not in email: #Check if the email is a part of company domain.
        print(f"Invalid domain for {name}: {email}")
        continue

    #Generate Username
    if len(parts) >=2 : #Check if the employee has more than one name
        username = parts[0] + "." + parts[1] #Generate username in the form <first_name>"."<second_name>
    else:
        username = parts[0]

    print(f"Name: {name} | Email : {email} | Username : {username}")