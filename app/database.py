from sqlalchemy import create_engine  #creates a db engine connection
from sqlalchemy.orm import sessionmaker, declarative_base #sessionmaker creates sessions to interact with the db, declarative_base is a base class for model classes

DATABASE_URL = "sqlite:///./wallet.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #creates a db engine connection and check same thread is required for sqlite to allow multi threads
SessionLocal = sessionmaker(bind=engine) #creates a session factory that will always connect to engine bind->binds the sessionmaker to db
Base = declarative_base() #base class for our models to inherit

def get_db():
    db = SessionLocal()
    try:
        yield db #Give this DB session to the route, let the route use it, and AFTER route completes, come back and execute the finally block.
    finally:
        db.close()
