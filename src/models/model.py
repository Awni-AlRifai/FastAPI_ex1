from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


        
class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Customer(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    age: int
    gender: Gender
    adult: bool
    # address_id: Optional[int]
    
class CustomerUpdate(BaseModel):
    first_name:Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    age: Optional[int]
    gender: Optional[Gender]
    adult: Optional[bool]
    



class Address(BaseModel):
    id: Optional[UUID]
    phone: str
    email: str
    country: str
    city: str
    street: str
    
class AddressUpdate(BaseModel):
    phone: Optional[str]
    email: Optional[str]
    country: Optional[str]
    city: Optional[str]
    street: Optional[str]
    
