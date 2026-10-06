from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            print("You do not have permission to access this function.")
            return None
        else:
            return func(user_role)  
    return wrapper


@require_admin
def access_sensitive_data(user_role):
    print("Sensitive data accessed!")

access_sensitive_data('admin')  # This will work
# access_sensitive_data('user')  # This will raise a PermissionError