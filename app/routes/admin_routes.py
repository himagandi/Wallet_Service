from fastapi import APIRouter, Depends #APIRouter groups admin endpoints; Depends injects DB session.
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import AdminLogin
from app.interfaces.admin_interface import *
from app.simple_auth import login_admin #Used to store logged-in admin in global variable.

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/create")
def create(data: AdminLogin, db: Session = Depends(get_db)):
    return create_admin_interface(db, data)

@router.post("/login")
def login(data: AdminLogin, db: Session = Depends(get_db)):
    admin = login_admin_interface(db, data)
    if not admin:
        return {"message": "Invalid admin credentials"}
    login_admin(admin)
    return {"message": "Admin logged in successfully"}
