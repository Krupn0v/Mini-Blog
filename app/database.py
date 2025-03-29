from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv('.env')
login = os.getenv('login')
password  = os.getenv('password')
base = os.getenv('base')
host = os.getenv('host')

url_db = f"postgresql://{login}:{password}@{host}:5432/{base}"
engine = create_engine(url_db)
localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()