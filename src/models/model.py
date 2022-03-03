from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Customer(BaseModel):

    id: int
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address_id: int


class Address(BaseModel):
    id: int
    phone: int
    email: str
    country: str
    city: str
    street: str
