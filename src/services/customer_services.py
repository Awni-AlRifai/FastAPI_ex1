from typing import List
from uuid import uuid4

from fastapi import HTTPException, status
from src.db.db import fake_customer_db, fake_address_db
from src.models.model import Customer

# we should handle the results seperately


def get_all() -> list:
    """ get all customer from customers table

    Returns:
        List: returns a list of customers
    """
    return fake_customer_db


def get_customer(id: int):
    customers = fake_customer_db
    for customer in customers:
        if customer['id'] == id:
            return customer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find was not found')


def create_customer(customer: Customer) -> str:
    """create customers

    Args:
        customer (model.Customer): accepts Customer object

    Returns:
        str: returns simple success message
    """
    customer.id = uuid4()
    fake_customer_db.append(dict(customer))
    return "created successfully"


def update_customer(id: int, customer: Customer) -> str:
    """update customers based on id given and customer object given

    Args:
        id (int): accepts customer id of int type
        customer (Customer): accepts customer dict of type Customer

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        str: returns simple success message
    """

    customers = fake_customer_db
    for saved_customer in customers:
        if saved_customer['id'] == id:
            saved_customer.update(dict(customer))
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')


def delete_customer(id: int):
    # should update optional fields
    """delete customer and his address based on id and address_id

    Args:
        id (int): accepts a customer id of int type

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    customers = fake_customer_db
    addresses = fake_address_db
    # removing global will raise 'local variable 'customer_addres_id' referenced before assignment'
    global customer_addres_id
    for customer in customers:
        if customer['id'] == id:
            customer_addres_id = customer['address_id']
            customers.remove(customer)
    if(not customer_addres_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The customer you are trying to update was not found')
    for address in addresses:
        if address['id'] == customer_addres_id:
            addresses.remove(address)
