from fastapi import APIRouter, status, HTTPException

from ..models import model
from ..db import db


router = APIRouter()


@router.get('/api/v1/customer', status_code=status.HTTP_202_ACCEPTED)
def all_customers():
    return db.fake_customer_db


@router.get('/api/v1/customer/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_customer(id: int):
    customers = db.fake_customer_db
    for customer in customers:
        if customer['id'] == id:
            return customer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to find was not found')


@router.post('/api/v1/customer', status_code=status.HTTP_201_CREATED)
def create_customer(customer: model.Customer):
    db.fake_customer_db.append(customer)
    return 'created successfully'


@router.put('/api/v1/customer/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update_customer(id: int, customer: model.Customer):
    customers = db.fake_customer_db
    for saved_customer in customers:
        if saved_customer['id'] == id:
            saved_customer = customer
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')


@router.delete('/api/v1/customer/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete_customer(id: int):
    customers = db.fake_customer_db
    for saved_customer in customers:

        if saved_customer['id'] == id:
            customers.remove(saved_customer)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The customer you are trying to update was not found')
