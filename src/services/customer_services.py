from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.model import Customer, CustomerUpdate
from src.db.schemas import Customer as CustomerSchema

def get_all(db:Session) -> list:
    """get all customer from customers table

    Args:
        db (Session):local session of databse

    Returns:
        list: returns a list of customers
    """
    return db.query(CustomerSchema).all()


def get_customer(id: UUID,db:Session) -> Customer:
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
                        detail=f'The customer you are trying to update was not found')
        
    return saved_customer.first()

   


def create_customer(customer: Customer,db:Session) -> CustomerSchema:
    """create customers

    Args:
        customer (model.Customer): accepts Customer object
        db (Session):local session of databse

    Returns:
         CustomerSchema: returns created customer 
    """
    new_customer=CustomerSchema(
        first_name=customer.first_name,
        last_name=customer.last_name,
        age=customer.age,
        gender=customer.gender,
        adult=customer.adult
        )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def update_customer(id: UUID, customer: CustomerUpdate,db:Session) -> CustomerSchema:
  
    """update customers based on id given and customer object given

    Args:
        id (UUID): accepts customer id of UUID type
        customer (Customer): accepts customer dict of type Customer
        db (Session):local session of databse

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        CustomerSchema: returns updated customer
    """

    saved_customer=db.query(CustomerSchema).filter(CustomerSchema.id==id)
    if not saved_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')
  
    saved_customer=saved_customer.first()
    saved_customer.first_name=customer.first_name or saved_customer.first_name,
    saved_customer.last_name=customer.last_name or saved_customer.last_name,
    saved_customer.age=customer.age or saved_customer.age
    saved_customer.adult=customer.adult or saved_customer.adult
    saved_customer.gender=customer.gender or saved_customer.gender
    db.commit()
    db.refresh(saved_customer)
    
    return saved_customer
        
    
    
        
    
   
    


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
   
