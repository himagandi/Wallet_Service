from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import *
from app.interfaces.user_interface import *
from app.simple_auth import get_logged_admin, get_logged_user, login_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user_route(data: UserCreate, db: Session = Depends(get_db)):
    return create_user_interface(db, data)

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = login_user_interface(db, data)
    if not user:
        return {"message": "Invalid login"}
    login_user(user)
    return {"message": "User logged in"}

@router.get("/")
def list_users_route(db: Session = Depends(get_db)):
    admin = get_logged_admin()
    if not admin:
        return {"message": "Only admin can view all users"}
    return list_users_interface(db)

@router.put("/{user_id}")
def update_user_route(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = get_logged_user()
    if not user or user.id != user_id:
        return {"message": "Not allowed to edit another user"}
    return update_user_interface(db, user_id, data)

@router.delete("/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    admin = get_logged_admin()
    if not admin:
        return {"message": "Only admin can delete users"}
    return delete_user_interface(db, user_id)
