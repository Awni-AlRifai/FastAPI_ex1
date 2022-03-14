from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from src.db.schemas import User
from src.models.model import UserLogin
from passlib.context import CryptContext
from src.services.oauth2 import create_access_token

pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")



def user_login(user_credentials:UserLogin,db:Session):
    """login user

    Args:
        user_credentials (UserLogin): accepts the email and the password
        db (Session): _description_

    Raises:
        HTTPException: raised when the email is not found
        HTTPException: raised when the password is incorrect

    Returns:
        _type_: return jwt access token
    """
    user=db.query(User).filter(User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')
    if not verify_password(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Credentials')
    
    access_token=create_access_token(data={'user_id':str(user.id)})
    
    
    return {'access_token':access_token,'token_type':'bearer'}


def hash(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify( plain_password,hashed_password)
