from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.model import BaseAddress, GetAddress
from src.db.schemas import Address as AddressSchema,Customer as CustomerSchema


def get_all(db:Session) -> list:
    """get all address records from table address

    Returns:
        list: returns a list of dict if type address
    """

    return db.query(AddressSchema).all()


def get_address_id_from_customer(id: UUID,db:Session) -> UUID:
    """ accepts customer id and returns address id related to the customer 

    Args:
        id (UUID): accepts customer_id of id type UUID

    Returns:
        UUID: returns address id 
    """
    customer=db.query(CustomerSchema).filter(CustomerSchema.id==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find address to was not found')
    return customer.first().id


def get_address(id: UUID,db:Session) -> GetAddress:
    """get a specific address from an id

    Args:
        id (UUID): accepts an address of id type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Address: return a dict of type Address
    """
    address = validate_address(id,db)
    if not address.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to find was not found')
    return address.first()
   


def create_address(address: BaseAddress,db:Session) -> GetAddress:
    """create a record in the table address 

    Args:
        address (Address): accepts a dict of type Address

    Returns:
        Address: returns created Address
    """
    new_address=AddressSchema(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def update_address(id: UUID, address: BaseAddress,db:Session) -> GetAddress:
    """update the a specific Address based on id

    Args:
        id (UUID): Address id of type UUID
        address (Address): dict of Address

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Address: returns updated address
    """
    saved_address = validate_address(id,db)
    if not saved_address.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to find was not found')
    
    saved_address.update(address.dict(),synchronize_session=False)
    db.commit()
    return saved_address.first()

def delete_address(id: UUID,db:Session) -> None:
    """delete an address based on id

    Args:
        id (UUID): address id of type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    # should update optional fields
    address = validate_address(id,db)
    if not address.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to delete was not found')
    address.delete(synchronize_session=False)
    db.commit()

def validate_address(id:UUID,db:Session):
    """ Checks if the address exists in the database and returns the result

    Args:
        id (int): address id
        db (Session): db session to query the id

    Returns:
        query: returns a query result
    """
    query=db.query(AddressSchema).filter(AddressSchema.id==id)
    return query

    
   

   