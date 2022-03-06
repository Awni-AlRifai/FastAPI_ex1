

from uuid import uuid4
from src.models.model import Gender


fake_customer_db = [
    {"id": uuid4(), "first_name": "Mohammad", "last_name": "Ahamd", "age": 25,
        "gender": Gender.male, "adult": True, "address_id": 2, },
    {"id": uuid4(), "first_name": "Ali", "last_name": "Mousa", "age": 17,
     "gender": Gender.male, "adult": False, "address_id": 0, },
    {"id": uuid4(), "first_name": "Fadwa", "last_name": "Kareem", "age": 22,
     "gender": Gender.female, "adult": True, "address_id": 3, },
    {"id": uuid4(), "first_name": "Salwa", "last_name": "Belal", "age": 32,
     "gender": Gender.female, "adult": True, "address_id": 1, },
]
fake_address_db = [
    {"id": uuid4(), "phone": "0700000000", "email": "0@gmail.com",
        "country": "Jordan", "city": "Amman", "street": "Maka Street", },
    {"id": uuid4(), "phone": "07111111111", "email": "1@gmail.com",
     "country": "Jordan", "city": "Zarqa", "street": "Sadaa Street", },
    {"id": uuid4(), "phone": "0722222222", "email": "2@gmail.com",
     "country": "Jordan", "city": "Irbid", "street": "University Street", },
    {"id": uuid4(), "phone": "0733333333", "email": "3@gmail.com",
     "country": "Jordan", "city": "Jarash", "street": "Jarash Street", }
]
