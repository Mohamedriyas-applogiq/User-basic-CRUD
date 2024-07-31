from fastapi import Depends
from sqlalchemy.orm import Session
from app.api.user.schema import *
from configuration.config import *
from app.api.user.controller import *


@router.post("/users/", response_model=UserResponse)
def create_user_router(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_controller(db,user)

@router.get("/users/", response_model=list[UserResponse])
def read_users_router(db: Session = Depends(get_db),skip: int = 0, limit: int = 100):
    return  get_users_controller(db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=UserResponse)
def  read_user(user_id:int,db: Session = Depends(get_db)):
     return get_user_controller(db,user_id=user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id:int, user_update: UserUpdate,db: Session = Depends(get_db)):
    return update_user_controller(db,user_id=user_id, user_update=user_update)
   
@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id:int,db: Session = Depends(get_db)):
    return delete_user_controller(db,user_id=user_id)


@router.post("/users/{user_id}/items/")
def create_item(item:ItemCreate,user_id:int,db:Session= Depends(get_db)):
    return create_user_item_controller(item,user_id,db)


@router.get("/items/")
def read_items(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return read_item_controller(db,skip,limit)

@router.put("/items/")
def update_item(item_id:int,item_update:ItemUpdate,db:Session=Depends(get_db)):
    return update_item_controller(item_id,item_update,db)   


@router.delete("/item/")
def deleting_item(item_id,db:Session=Depends(get_db)):
    return delete_item_controller(item_id,db)

