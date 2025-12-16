from app.services.user_service import *

def create_user_interface(db, data):
    return create_user(db, data.name, data.email, data.password)

def login_user_interface(db, data):
    return verify_user(db, data.email, data.password)

def update_user_interface(db, user_id, data):
    return update_user(db, user_id, data.name, data.email)

def delete_user_interface(db, user_id):
    return delete_user(db, user_id)

def list_users_interface(db):
    return list_users(db)
