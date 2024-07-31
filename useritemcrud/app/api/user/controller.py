from fastapi import HTTPException
from app.api.user.service import *
from configuration.config import *

def create_user_controller(db,user: UserCreate):
    try:
        db_user = create_user(db, user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
            

def get_users_controller(db,skip,limit):
    data=get_users(db,skip,limit)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data
def get_user_controller(db,user_id):
    data=get_user(db,user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data

def update_user_controller(db,user_id, user_update):
    data=update_user(db,user_id,user_update)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data


def delete_user_controller(db,user_id):
    data=delete_user(db,user_id=user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data

def create_user_item_controller(item,user_id,db):
    data=create_user_item(item,user_id,db)
    if not data:
        raise HTTPException(status_code=400, detail="Bad request")
    return data



def read_item_controller(skip,limit,db):
    data=get_items(skip,limit,db)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    return data

def update_item_controller(item_id,item_update,db):
    data=update_item(item_id,item_update,db)
    if not data:
        raise HTTPException(status_code=400, detail="Bad request")
    return data

def delete_item_controller(item_id,db):
    data=delete_item(item_id,db)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    return data    
