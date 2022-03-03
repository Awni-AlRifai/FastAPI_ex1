from typing import List
from fastapi import HTTPException, status

from src.models.model import Customer
from src.db.db import fake_customer_db

# we should handle the results seperately


def get_all() -> list:
    """_summary_

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
    """_summary_

    Args:
        customer (model.Customer): accepts Customer object

    Returns:
        str: returns simple success message
    """
    fake_customer_db.append(customer)
    return "created successfully"


def update_customer(id: int, customer: Customer) -> str:
    """_summary_

    Args:
        id (int): accepts customer id of int type
        customer (Customer): accepts customer dict of type Customer

    Raises:
        HTTPException: raises and exception when the id provided is not found

    Returns:
        str: returns simple success message
    """

    customer = fake_customer_db
    for saved_customer in customer:
        if saved_customer['id'] == id:
            saved_customer = customer
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')


def delete_customer(id: int):
    # should update optional fields
    """_summary_

    Args:
        id (int): accepts a customer id of int type

    Raises:
        HTTPException: raises and exception when the id provided is not found
    """
    customers = fake_customer_db
    for saved_customer in customers:
        if saved_customer['id'] == id:
            customers.remove(saved_customer)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')
