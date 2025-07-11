from decorator_example import *


#Simulating Calls.
def simulate_delete_user(is_authenticated, user):
    current_user["authenticated"] = is_authenticated
    delete_user(user)



simulate_delete_user(True, "user123")
simulate_delete_user(False, "user456")
simulate_delete_user(True, "user123") # Should hit rate limit

view_reports()
view_reports()