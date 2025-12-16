from app.models import User, Transaction
from sqlalchemy.orm import Session

def recharge(db, user_id, amount):
    user = db.query(User).filter(User.id == user_id).first()
    if not user: return None
    user.balance += amount
    db.commit()

    txn = Transaction(user_id=user_id, type="CREDIT", subtype="RECHARGE", amount=amount)
    db.add(txn)
    db.commit()

    return user

def withdraw(db, user_id, amount):
    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.balance < amount: return None

    user.balance -= amount
    db.commit()

    txn = Transaction(user_id=user_id, type="DEBIT", subtype="WITHDRAW", amount=amount)
    db.add(txn)
    db.commit()

    return user

def spend(db, user_id, amount):
    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.balance < amount: return None

    user.balance -= amount
    reward = int(amount // 100) * 10
    user.reward_points += reward

    db.commit()

    txn = Transaction(user_id=user_id, type="DEBIT", subtype="SPENDING", amount=amount, reward_points_earned=reward)
    db.add(txn)
    db.commit()

    return user
