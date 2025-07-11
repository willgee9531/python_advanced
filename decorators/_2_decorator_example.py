from functools import wraps
import datetime

# Decorators real world application

"""simulate logged-in user"""
current_user = {
    "username": "admin",
    "authenticated": False,
    "role": "admin",
    "call_count": {}
}




def require_auth(func):
    """ 
    Authentication Decorator:
    This decorator checks if the user is
    authenticated before running any restricted command.
    """
    def wrapper(*args, **kwargs):
        if current_user["authenticated"]:
            return func(*args, **kwargs)
        else:
            print("Error: You must be logged in to perform this action.")
    return wrapper



def log_action(func):
    """
    Logging Decorator:
    This decorator logs the function name and
    arguments to show what action was taken.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] {current_user['username']} called '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper


def rate_limit(limit=2):
    """
    Rate Limiting Decorator:
    Limit each function to being called
    only 2 times per user for this simulation.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            user_counts = current_user["call_count"]
            if user_counts.get(name, 0) >= limit:
                print(f"Rate limit reached for {name}")
                return
            user_counts[name] = user_counts.get(name, 0) + 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


"""
Protected Functions:
We now apply all three
decorators on admin-only functions
"""
@require_auth
@log_action
@rate_limit(limit=2)
def delete_user(user_id):
    print(f"User - {user_id} deleted.")

@require_auth
@log_action
def view_reports():
    print("Displaying system reports...")



