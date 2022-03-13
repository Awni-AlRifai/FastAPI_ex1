import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey,Integer,String,Enum,Boolean
from src.db import Base
from src.models.model import Gender
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__="customers"
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    first_name=Column(String)
    middle_name=Column(String)
    last_name=Column(String)
    age=Column(Integer)
    gender=Column(Enum(Gender))
    adult=Column(Boolean)
    address_id=Column(UUID,ForeignKey('addresses.id'),nullable=True)
    address=relationship('Address',back_populates='customer')
    
class Address(Base):
    __tablename__="addresses"
    ##as_uuid=False – if True, values will be interpreted as Python uuid objects, converting to/from string via the DBAPI.
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    phone=Column(String)
    email=Column(String)
    country=Column(String)
    city=Column(String)
    street=Column(String)
    customer=relationship('Customer',back_populates='address')
    
   
  
    
    
    
