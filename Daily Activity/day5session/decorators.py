def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print(f"{user} is not an admin. Access denied.")
            return
        return func(*args, **kwargs)
    return wrapper

@require_admin
def delete_user(user_id):
    print(f"User {user_id} deleted.")
    return True

delete_user("admin", 123)  
delete_user("guest", 123) 