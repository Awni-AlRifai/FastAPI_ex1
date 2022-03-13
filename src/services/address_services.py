from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.model import Address, AddressUpdate
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
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find address to was not found')
    return customer.first().id


def get_address(id: UUID,db:Session) -> Address:
    """get a specific address from an id

    Args:
        id (UUID): accepts an address of id type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Address: return a dict of type Address
    """
    address = db.query(AddressSchema).filter(AddressSchema.id==id)
    if not address:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to find was not found')
    return address.first()
   


def create_address(address: Address,db:Session) -> Address:
    """create a record in the table address 

    Args:
        address (Address): accepts a dict of type Address

    Returns:
        Address: returns created Address
    """
    new_address=AddressSchema(phone=address.phone,
        email=address.email,
        country=address.country,
        city=address.city,
        street=address.street)
    
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


def update_address(id: UUID, address: AddressUpdate,db:Session) -> Address:
    """update the a specific Address based on id

    Args:
        id (UUID): Address id of type UUID
        address (Address): dict of Address

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Address: returns updated address
    """
    saved_address = db.query(AddressSchema).filter(AddressSchema.id==id)
    if not address:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to find was not found')
    saved_address=saved_address.first()
    saved_address.phone=address.phone or saved_address.phone,
    saved_address.email=address.email or saved_address.email,
    saved_address.country=address.country or saved_address.country
    saved_address.city=address.city or saved_address.city
    saved_address.street=address.street or saved_address.street
    db.commit()
    db.refresh(saved_address)
    return saved_address

def delete_address(id: UUID,db:Session) -> None:
    """delete an address based on id

    Args:
        id (UUID): address id of type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    # should update optional fields
    address = db.query(AddressSchema).filter(AddressSchema.id==id)
    if not address:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to update was not found')
    address.delete(synchronize_session=False)
    db.commit()

   

   