from fastapi import HTTPException, status
from sqlalchemy import null

from src.models.model import Adress
from src.db.db import fake_address_db
# we should handle the results seperately


def get_all() -> list:
    """get all address records from table address

    Returns:
        list: returns a list of dict if type address
    """

    return fake_address_db


def get_address(id: int) -> Adress:
    """get a specific address from an id

    Args:
        id (int): accepts an address of id type int

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        Adress: return a dict of type Address
    """
    adressses = fake_address_db
    for adress in adressses:
        if adress['id'] == id:
            return adress
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to find was not found')


def create_address(adress: Adress) -> str:
    """create a record in the table address 

    Args:
        adress (Adress): accepts a dict of type Address

    Returns:
        str: returns success message
    """
    fake_address_db.append(adress)
    return "created successfully"


def update_address(id: int, address: Adress) -> str:
    """update the a specific Address based on id

    Args:
        id (int): Address id of type int
        address (Adress): dict of Address

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        str: simple success message
    """
    address = fake_address_db
    for saved_address in address:
        if saved_address['id'] == id:
            saved_address = address
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')


def delete_address(id: int) -> None:
    """delete an address based on id

    Args:
        id (int): address id of type int

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    # should update optional fields
    adresss = fake_address_db
    for saved_adress in adresss:
        if saved_adress['id'] == id:
            adresss.remove(saved_adress)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')
