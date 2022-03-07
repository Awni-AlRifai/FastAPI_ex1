import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,Integer,String,Enum,Boolean
from src.db.db import Base
from src.models.model import Gender

class Customer(Base):
    __tablename__="customers"
    ##as_uuid=False – if True, values will be interpreted as Python uuid objects, converting to/from string via the DBAPI.
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    first_name=Column(String)
    last_name=Column(String)
    age=Column(Integer)
    gender=Column(Enum(Gender))
    adult=Column(Boolean)
    address_id=Column(Integer,nullable=True)
    
    
    
    
