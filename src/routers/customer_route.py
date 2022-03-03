from fastapi import APIRouter, status, HTTPException

from ..models import model
from ..db import db
from ..services import customer_services


router = APIRouter()


@router.get('/api/v1/customer', status_code=status.HTTP_202_ACCEPTED)
def all_customers():
    return customer_services.get_all()


@router.get('/api/v1/customer/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_customer(id: int):
    return customer_services.get_customer(id)


@router.post('/api/v1/customer', status_code=status.HTTP_201_CREATED)
def create_customer(customer: model.Customer):
    return customer_services.create_customer(customer)


@router.put('/api/v1/customer/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update_customer(id: int, customer: model.Customer):
    return customer_services.update_customer(customer)


@router.delete('/api/v1/customer/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete_customer(id: int):
    return customer_services.delete_customer(id)
