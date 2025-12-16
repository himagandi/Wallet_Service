from app.services.wallet_service import recharge, withdraw, spend

def recharge_interface(db, data):
    return recharge(db, data.user_id, data.amount)

def withdraw_interface(db, data):
    return withdraw(db, data.user_id, data.amount)

def spend_interface(db, data):
    return spend(db, data.user_id, data.amount)
