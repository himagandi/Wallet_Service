from fastapi import FastAPI
from app.database import Base, engine
from app.routes.user_routes import router as user_router
from app.routes.admin_routes import router as admin_router
from app.routes.wallet_routes import router as wallet_router

Base.metadata.create_all(bind=engine) #creates all tables in the database which are defined as subclasses of Base
#metadata-table definitions contains columns,table names and all
app = FastAPI(title="Wallet Service") #initialize FastAPI app

@app.get("/")
def home():
    return {"message": "API Running"} #root endpoint to check if API is running

#include routers for admin,user and wallet
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(wallet_router)




