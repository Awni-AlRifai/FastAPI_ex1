from typing import List
from src.models.model import BaseUser,GetUser
from sqlalchemy.orm import Session
from src.db.schemas import User
from src.models.model import CreateUser
from src.services.auth_services import hash



def create_user(user:CreateUser,db:Session)->GetUser:
    user.password=hash(user.password)
    new_user=User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session)->List[GetUser]:
    return db.query(User).all()

