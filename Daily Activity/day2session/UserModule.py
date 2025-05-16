'''module is .py file
module contains functions, classes and variables'''

user_info={}

def get_user_info():
    return user_info

def add_user_info(userId,userName,userEmail):
    user_info[userId]={
        "user_name" : userName,
        "user_email" : userEmail
    }
    print("Info added successfully!")

# def update_user_email(userId):
#     userInfo= user_info[userId]
#     print(f"Your Old Info : {user_info[userId]}")
#     userEmail = input("Enter New Email ID : ")
#     user_info.update({userId})
#     print(f"Updated Successfully : {user_info[userId]}")