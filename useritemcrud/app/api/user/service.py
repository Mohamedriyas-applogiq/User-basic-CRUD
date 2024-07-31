from app.api.user.model import *
from app.api.user.schema import *
from sqlalchemy.orm import Session

def create_user(db:Session, user: UserCreate):
    
    fake_hashed_password = user.password 
    db_user = User(email=user.email,password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_user(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_users_by_email(db:Session,user_email:str):
    return db.query(User).filter(User.email==user_email).first()


def update_user(db:Session, user_id: int, user_update:UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    
    if user_update.username is not None:
        db_user.username = user_update.username
    if user_update.email is not None:
        db_user.email = user_update.email
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

def create_user_item(item:ItemCreate, user_id: int,db:Session):
    db_user = Item(**item.dict(), owner_id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        return None
    if item_update.name is not None:
        db_item.name = item_update.name
    if item_update.description is not None:
        db_item.description = item_update.description
    
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(item_id: int,db:Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item
    return None