from uuid import UUID, uuid4
from fastapi import HTTPException, status
from sqlalchemy import null

from src.models.model import Address
from src.db.db import fake_address_db, fake_customer_db
# we should handle the results seperately


def get_all() -> list:
    """get all address records from table address

    Returns:
        list: returns a list of dict if type address
    """

    return fake_address_db


def get_address_id_from_customer(id: UUID) -> UUID:
    """ accepts customer id and returns address id related to the customer 

    Args:
        id (UUID): accepts customer_id of id type UUID

    Returns:
        UUID: returns address id 
    """
    customers = fake_customer_db
    for customer in customers:
        if customer['id'] == id:
            return customer['id']

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find address to is not found')


def get_address(id: UUID) -> Address:
    """get a specific address from an id

    Args:
        id (UUID): accepts an address of id type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Address: return a dict of type Address
    """
    addressses = fake_address_db
    for address in addressses:
        if address['id'] == id:
            return address
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to find was not found')


def create_address(address: Address) -> str:
    """create a record in the table address 

    Args:
        address (Address): accepts a dict of type Address

    Returns:
        str: returns success message
    """
    address.id = uuid4()
    fake_address_db.append(address)
    return address


def update_address(id: UUID, address: Address) -> str:
    """update the a specific Address based on id

    Args:
        id (UUID): Address id of type UUID
        address (Address): dict of Address

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        str: simple success message 
    """
    addresses = fake_address_db
    for saved_address in addresses:
        if saved_address['id'] == id:
            saved_address.update(dict(address))
            return saved_address
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to update was not found')


def delete_address(id: UUID) -> None:
    """delete an address based on id

    Args:
        id (UUID): address id of type UUID

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    # should update optional fields
    addresss = fake_address_db
    for saved_address in addresss:
        if saved_address['id'] == id:
            addresss.remove(saved_address)
            return "Deleted Successfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The address you are trying to update was not found')
