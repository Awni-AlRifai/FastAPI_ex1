from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.model import BaseCustomer, GetCustomer
from src.db.schemas import Customer as CustomerSchema
from src.services.address_services import validate_address

def get_all(db:Session) -> list:
    """get all customer from customers table

    Args:
        db (Session):local session of databse

    Returns:
        list: returns a list of customers
    """
    return db.query(CustomerSchema).all()


def get_customer(id: UUID,db:Session) -> GetCustomer:
    """ gets cusotmer id from customers table and returns the customer that have the same id

    Args:
        id (UUID): customer id of type UUID
        db (Session):local session of databse

    Raises:
        HTTPException: raises not found exception when the customer id is not found

    Returns:
        CustomerSchema: returns customer of type Customer
    """
    saved_customer=db.query(CustomerSchema).filter(CustomerSchema.id==id)
    if not saved_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find was not found')
        
    return saved_customer.first()

   


def create_customer(customer: BaseCustomer,db:Session) -> GetCustomer:
    """create customers

    Args:
        customer (model.Customer): accepts Customer object
        db (Session):local session of databse
        
    Raises:
        HTTPException: raises an exception when the address_id is not valid

    Returns:
         CustomerSchema: returns created customer 
    """
    #check if address id is available
    
    if customer.address_id!=None:
        if not validate_address(customer.address_id,db).first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The address_id {customer.address_id} was not found')
        
        
    new_customer=CustomerSchema(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def update_customer(id: UUID, customer: BaseCustomer,db:Session) -> GetCustomer:
  
    """update customers based on id given and customer object given

    Args:
        id (UUID): accepts customer id of UUID type
        customer (Customer): accepts customer dict of type Customer
        db (Session):local session of databse

    Raises:
        HTTPException: raises an exception when the address_id is not valid
        HTTPException: raises and exception when the id provided is not found

    Returns:
        CustomerSchema: returns updated customer
    """
    
    if customer.address_id:
        if not validate_address(customer.address_id,db).first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The address_id {customer.address_id} was not found')

    saved_customer=db.query(CustomerSchema).filter(CustomerSchema.id==id)
    if not saved_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')
    
    saved_customer.update(customer.dict(),synchronize_session=False)
    db.commit()
    return saved_customer.first()
    
def delete_customer(id: UUID,db:Session)->None:
    # should update optional fields
    """delete customer and his address based on id and address_id

    Args:
        id (UUID): accepts a customer id of UUID type

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    customer=db.query(CustomerSchema).filter(CustomerSchema.id==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The customer with the id {id} was not found')
    #remember to delete the address also when we add the address table
    customer.delete(synchronize_session=False)
    db.commit()


    
    
   
