from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Customer(BaseModel):
    id: Optional[UUID]
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address_id: int


class Address(BaseModel):
    id: Optional[UUID]
    phone: str
    email: str
    country: str
    city: str
    street: str
