import UserModule



while True:
    print("Welcome to User Information System")
    print("1: Add new User")
    print("2: Display all user information")
    print("3. Update E-Mail")
    print("4. Exit")
    choice = int(input("Enter the preffered choice : "))
    if choice == 2:
        print(UserModule.get_user_info())
    elif choice == 1:
        userId = int(input("Enter User Id : "))
        userName = input("Enter User Name : ")
        userEmail = input("Enter Email : ")
        UserModule.add_user_info(userId, userName, userEmail)
    elif choice == 3:
        userId = int(input("Enter User Id : "))
        UserModule.update_user_email(userId)
    elif choice == 4:
        print("Exitting Program...")
        break
    else:
        print("Invalid Choise, Try Again.")
        continue
