from datetime import datetime

def logging_func(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        user_logged = kwargs.get("user")
        rv = func(**kwargs)
        end_time = datetime.now()
        total_time = end_time - start_time

        print(f"[{end_time}] - {user_logged}'s action: {func.__name__!r}")
        print(f"Function Runtime: {total_time.total_seconds():.4f}s")
        return rv
    return wrapper

@logging_func
def delete_post(user="admin"):
    print(f"{user} deleted the post.")
    return {
        "status": "success",
        "status_code": 200
    }

print(delete_post(user="willgee9531"))