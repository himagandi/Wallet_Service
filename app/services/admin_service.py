from app.models import Admin
from sqlalchemy.orm import Session

def create_admin(db: Session, username: str, password: str):
    admin = Admin(username=username, password=password)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def verify_admin(db: Session, username: str, password: str):
    return db.query(Admin).filter(Admin.username == username, Admin.password == password).first()
