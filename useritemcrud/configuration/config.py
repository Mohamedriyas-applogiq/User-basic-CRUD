from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
Base=declarative_base()

DATA_BASE_URL="postgresql://postgres:12345@localhost/userandproduct"
engine=create_engine(DATA_BASE_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

router = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()