from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import WalletOperation
from app.interfaces.wallet_interface import *
from app.simple_auth import get_logged_admin, get_logged_user

router = APIRouter(prefix="/wallet", tags=["Wallet"])

@router.post("/recharge")
def recharge_route(data: WalletOperation, db: Session = Depends(get_db)):
    admin = get_logged_admin()
    user = get_logged_user()

    if not admin and not user:
        return {"message": "Login required"}

    if user and user.id != data.user_id:
        return {"message": "Users cannot recharge others"}

    result = recharge_interface(db, data)
    if not result:
        return {"message": "User not found"}
    return {"message": "Recharge successful", "balance": result.balance}

@router.post("/withdraw")
def withdraw_route(data: WalletOperation, db: Session = Depends(get_db)):
    user = get_logged_user()
    admin = get_logged_admin()

    if not admin and not user:
        return {"message": "Login required"}

    if user and user.id != data.user_id:
        return {"message": "Cannot withdraw from another user"}

    result = withdraw_interface(db, data)
    if not result:
        return {"message": "Insufficient funds"}
    return {"message": "Withdraw successful", "balance": result.balance}

@router.post("/spend")
def spend_route(data: WalletOperation, db: Session = Depends(get_db)):
    user = get_logged_user()
    admin = get_logged_admin()

    if not admin and not user:
        return {"message": "Login required"}

    if user and user.id != data.user_id:
        return {"message": "Cannot spend for another user"}

    result = spend_interface(db, data)
    if not result:
        return {"message": "Insufficient balance"}

    return {
        "message": "Spend successful",
        "balance": result.balance,
        "reward_points": result.reward_points
    }
