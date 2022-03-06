from enum import Enum
from uuid import uuid4
from pydantic import BaseModel


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Customer(BaseModel):
    id = uuid4()
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address_id: int


class Address(BaseModel):
    id = uuid4()
    phone: int
    email: str
    country: str
    city: str
    street: str
