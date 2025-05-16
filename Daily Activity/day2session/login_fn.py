''' Login Validation - Allow only the username "admin" and password "1234" '''

#Defining the login validation function
def admin_login(userName, passWord):
    if userName == "admin" and passWord == "1234": #Checking the condition
        print(f"Welcome {userName}, Access Granted!")
    else :
        print("Unauthorized Access, Access Denied!")

#Calling the function in the main thread
if __name__=="__main__":
    userName = input("Enter User Name : ")
    passWord = input("Enter Password : ")
    admin_login(userName, passWord)