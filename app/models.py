from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float, default=0)
    reward_points = Column(Integer, default=0)
    status = Column(String, default="active") #used for soft delete

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    type = Column(String)
    subtype = Column(String)
    amount = Column(Float)
    reward_points_earned = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
