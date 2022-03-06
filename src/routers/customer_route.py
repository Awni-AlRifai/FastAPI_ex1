from fastapi import APIRouter, status

from src.models.model import Customer
from src.services.customer_services import create_customer, get_all, update_customer, delete_customer, get_customer


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
def all_customers():
    return get_all()


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create(customer: Customer):
    return create_customer(customer)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update(id: int, customer: Customer):
    return update_customer(id, customer)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete(id: int):
    return delete_customer(id)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_customer(id: int):
    return get_customer(id)
