current_admin = None
current_user = None

def login_admin(admin):
    global current_admin #use the variable defined outside the function or else it will create a local variable inside
    current_admin = admin

def login_user(user):
    global current_user
    current_user = user

def get_logged_admin():
    return current_admin

def get_logged_user():
    return current_user
