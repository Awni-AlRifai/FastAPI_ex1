from typing import List
from fastapi import APIRouter,status,Depends
from src.models.model import CreateUser,GetUser
from sqlalchemy.orm import Session
from src.db.db import get_db
from src.services.user_services import create_user,get_all

router=APIRouter()

@router.post('/create',status_code=status.HTTP_201_CREATED,response_model=GetUser)
def create(user:CreateUser,db:Session=Depends(get_db)):
    return create_user(user,db)

@router.get('',status_code=status.HTTP_200_OK,response_model=List[GetUser])
def all(db:Session=Depends(get_db)):
    return get_all(db)

