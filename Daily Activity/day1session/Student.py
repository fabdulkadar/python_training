""" read stud id, 3 subject marks, find average, result and grade
    result is pass when all 3 subject marks are >=40 else fail
    if result is pass find grade based on average 
       when avg >=80 grade A+
       when avg between 60 to 79 grade A
       when avg between 40 to 59 grade A
       else grade needs improvement"""


#Data Entry
studId = int(input("Enter Student ID : "))
print("Enter Marks out of 100")
stdMrk1 = int(input("Enter marks of Subject 1 : "))
stdMrk2 = int(input("Enter marks of Subject 2 : "))
stdMrk3 = int(input("Enter marks of Subject 3 : "))

stdAvg = (stdMrk1+stdMrk2+stdMrk3)/3 #Find Average

if stdMrk1 >=40 and stdMrk2>=40 and stdMrk3>=40: #Checking all marks are above or equal to 40
    result="Pass"
    #Grade Calculation
    if stdAvg >=80 and stdAvg <=100:
        grade="A+"
    elif stdAvg>=60 and stdAvg<80 :
        grade="A"
    elif stdAvg>=40 and stdAvg<60:
        grade="B"
else:
    result="Fail"
    grade="Needs Improvement"

#Output Results
print(f"Id : {studId} | Average: {stdAvg} | Result: {result} | Grade: {grade}")
