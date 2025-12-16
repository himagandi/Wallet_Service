from app.models import User
from sqlalchemy.orm import Session

def create_user(db: Session, name: str, email: str, password: str):
    user = User(name=name, email=email, password=password)
    db.add(user)
    db.commit()
    return user

def verify_user(db: Session, email: str, password: str):
    return db.query(User).filter(User.email == email, User.password == password).first()

def update_user(db, user_id, name, email):
    user = db.query(User).filter(User.id == user_id, User.status == "active").first()
    if not user: return None
    user.name = name
    user.email = email
    db.commit()
    return user

def delete_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user: return None
    user.status = "deleted"
    db.commit()
    return user

def list_users(db):
    return db.query(User).all()
