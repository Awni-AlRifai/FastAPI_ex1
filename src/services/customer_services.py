from fastapi import HTTPException, status

from ..models import model
from ..db import db

# we should handle the results seperately


def get_all():
    return db.fake_customer_db


def get_customer(id: int):
    customers = db.fake_customer_db
    for customer in customers:
        if customer['id'] == id:
            return customer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find was not found')


def create_customer(adress: model.Customer):
    db.fake_customer_db.append(adress)
    return "created successfully"


def update_customer(customer: model.Customer):
    customer = db.fake_customer_db
    for saved_customer in customer:
        if saved_customer['id'] == id:
            saved_customer = customer
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')


def delete_customer(id: int):
    # should update optional fields
    customers = db.fake_customer_db
    for saved_customer in customers:
        if saved_customer['id'] == id:
            customers.remove(saved_customer)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')
