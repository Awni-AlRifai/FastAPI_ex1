from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel,EmailStr
from datetime import datetime


        
class Gender(str, Enum):
    male = 'male'
    female = 'female'


class BaseCustomer(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    age: int
    gender: Gender
    adult: bool
    address_id:Optional[UUID]
    
    class Config():
        orm_mode=True
    
class GetCustomer(BaseCustomer):
    id:UUID
    
   
    

class BaseAddress(BaseModel):
    phone: str
    email: str
    country: str
    city: str
    street: str
    
    class Config():
        orm_mode=True
    
class GetAddress(BaseAddress):
    id:UUID

class BaseUser(BaseModel):
    name:str
    email:str

class BaseUser(BaseModel):
    name:str
    email:EmailStr
    
    class Config():
        orm_mode=True
class CreateUser(BaseUser):
    password:str
class GetUser(BaseUser):
    id:UUID
    created_at:datetime

class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
