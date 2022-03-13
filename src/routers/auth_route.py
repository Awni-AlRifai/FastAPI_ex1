from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.db.db import get_db
from src.models.model import UserLogin
from src.services.auth_services import user_login


router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials:UserLogin,db:Session=Depends(get_db)):
   return user_login(user_credentials,db)