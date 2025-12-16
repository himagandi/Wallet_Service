from app.services.admin_service import create_admin, verify_admin

def create_admin_interface(db, data):  #interface fun that takes db session and data from route and forwards to service
    return create_admin(db, data.username, data.password)

def login_admin_interface(db, data):
    return verify_admin(db, data.username, data.password)
